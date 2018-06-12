import sys
import urllib
from Scanner.papers.paper import Paper
import xml.etree.ElementTree as ET
# third party libraries
from bs4 import BeautifulSoup as bs
import json

ID_PREFIX = 'arxiv:'
namespace = "{http://www.w3.org/2005/Atom}"

class Scanner():

    def __init__(self, url,search_url):
        self.url = url
        self.search_url = search_url


    def _new_soupify(self, topic):
        url = self.url + "list/" + topic + "/new"
        data = urllib.request.urlopen(url)
        soup = bs(data.read(), "html.parser")
        soup.prettify()
        return soup

    def _new_parse(self, soup):
        papers = []
        
        for dt in soup.find_all('dt'):
            
            # dt element contains location/link information
            arxiv = dt.find(title='Abstract')
            arxiv_id = arxiv.string[len(ID_PREFIX):]  #get arxiv id
            
            # links to page and pdf
            page = self.url + arxiv['href'][1:]
            pdf = self.url + "pdf/" + arxiv_id   #get pdf link

            # dd element that contains content information
            dd = dt.next_sibling.next_sibling

            title = dd.find(class_='descriptor').next_sibling[1:].rstrip()

            # abstract may be absent
            abstract = None
            p = dd.div.p
            if p is not None and p.string is not None:
                abstract = p.string.replace('\n', ' ')
            
            # must account for multiple authors (with name and link to page)
            author_div = dd.find(class_='list-authors')
            authors = []
            for a in author_div.find_all('a'):
                author = { "name":a.string, "link": self.url + a['href'][1:] }
                authors.append(author["name"])
            paper = Paper(
                    title=title,
                    abstract=abstract,
                    arxiv_id=arxiv_id,
                    pdf=pdf,
                    page=page,
                    authors=authors
                    )
            papers.append(json.loads(paper.__str__()))

        return papers

    def get_new_public(self,topic):
        soup=self._new_soupify(topic)
        paper=self._new_parse(soup)
        return paper

    def _search_soupify(self,search_query,max_results):
        params = {
            "search_query": search_query,
            "max_results": max_results
        }
        url = self.search_url + "api/query?" + urllib.parse.urlencode(params)
        data = urllib.request.urlopen(url)
        tree = ET.parse(data)
        return tree

    def _search_parse(self, tree):
        papers = []
        count=0
        root = tree.getroot()

        # index 7 is starting point of entries
        for entry in root[7:]:
            page = entry.find(namespace + 'id').text.replace('\n', ' ').strip()
            title = entry.find(namespace + 'title').text.replace('\n', ' ').strip()
            summary = entry.find(namespace + 'summary').text.replace('\n', ' ').strip()

            authors = [author[0].text.replace('\n', ' ').strip() for author in entry.findall(namespace + 'author')]


            paper = Paper(
                title=title,
                abstract=summary,
                page=page,
                authors=authors
            )

            papers.append(json.loads(paper.__str__()))

        return papers

    def search(self,search_query, max_results):
        soup=self._search_soupify(search_query, max_results)
        paper=self._search_parse(soup)
        return paper

