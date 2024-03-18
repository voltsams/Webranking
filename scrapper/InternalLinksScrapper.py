import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin


class InternalLinksScrapper():
    def __init__(self):
        self.links = set()

    def base_url(self, url, with_path=False):
        parsed = urlparse(url)
        path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
        parsed = parsed._replace(path=path)
        parsed = parsed._replace(params='')
        parsed = parsed._replace(query='')
        parsed = parsed._replace(fragment='')
        return parsed.geturl()

    # TODO penser à gérer le cas des sous domaines

    def extract_internal_links(self, url):
        url_base = self.base_url(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href not in self.links:
                parsed_link = urlparse(href)
                if (parsed_link.netloc == '' and (re.compile("^/").match(href) or re.compile("^../").match(href)) or re.compile("^./").match(href)) or parsed_link.netloc == urlparse(url).netloc:
                    href = urljoin(url_base, href)
                    self.links.add(href)
