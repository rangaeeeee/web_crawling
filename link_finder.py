from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        self.current_tag = ""

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        self.current_tag = ""
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    self.current_tag = attribute
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def handle_data(self, data):
        if self.current_tag == 'href':
            pass
#            print(data)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
