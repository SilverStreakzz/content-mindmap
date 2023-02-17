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
    
    def create_mind_map():
        url = self.get_url()
        g = gt.Graph(directed=True)
        vprop = g.new_vertex_property("string")
        root_url = urlparse(url).scheme + '://' + urlparse(url).netloc
        v = g.add_vertex()
        vprop[v] = root_url
        visited = set([root_url])
        queue = [root_url]
        while queue:
            current_url = queue.pop(0)
            for link in get_internal_links(current_url):
                if link not in visited:
                    visited.add(link)
                    queue.append(link)
                    v2 = g.add_vertex()
                    vprop[v2] = urlparse(link).path
                    g.add_edge(v, v2)
        gt.graph_draw(g, vertex_text=vprop, vertex_font_size=18, output='mindmap.png')