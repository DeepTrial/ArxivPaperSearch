# @author Resnick Xing
# ArXivScanner
#

from Scanner.parsers.resolve_arxiv import Scanner


resolve=Scanner('http://arxiv.org/','http://export.arxiv.org/')

def search(content,max_result):
	result=resolve.search(content, max_results=max_result)
	return result

def new(topic='cs'):
	result=resolve.get_new_public(topic)
	return result

