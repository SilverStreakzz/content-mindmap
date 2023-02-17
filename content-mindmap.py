import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from graph_tools import Graph

class WebsiteContentMap:
    """
    This class is used to generate a mindmap of website content, based on a url.
    """
    def __init__(self, url):
        self.url = url
    
    def get_url(self):
        return self.url
    
    def get_internal_links(self):
        url = self.get_url()
        links = []
        r = requests.get(url)
        print(f'Getting links from {url}...')
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and urlparse(href).netloc == urlparse(url).netloc:
                links.append(href)
        return links