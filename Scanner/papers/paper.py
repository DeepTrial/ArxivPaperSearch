
import json


class Paper(object):
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.abstract = kwargs.get('abstract')
        self.arxiv_id = kwargs.get('arxiv_id')
        self.pdf = kwargs.get('pdf')
        self.page = kwargs.get('page')
        self.authors = kwargs.get('authors')

    def __str__(self):
        return json.dumps(
                {
                    "title": self.title,
                    "abstract": self.abstract,
                    "arxiv_id": self.arxiv_id,
                    "pdf": self.pdf,
                    "page": self.page,
                    "authors": self.authors
                }
        )

    def __repr__(self):
        return self.__str__()


