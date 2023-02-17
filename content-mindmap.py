import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import networkx as nx
import matplotlib.pyplot as plt


class WebsiteContentMap:
    """
    This class is used to generate a mindmap of website content, based on a url.
    """
    def __init__(self, url):
        self.url = url
        self.nodes = {}
        self.create_nodes()

    def get_url(self):
        return self.url

    def get_nodes(self) -> dict:
        return self.nodes

    def set_nodes(self, nodes: dict) -> None:
        self.nodes = nodes

    def create_nodes(self):
        url = self.get_url()
        links = {"inbound": [], "outbound": []}
        r = requests.get(url)
        print(f'Getting links from {url}...')
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                if urlparse(href).netloc == urlparse(url).netloc:
                    links["inbound"].append(href)
                else:
                    links["outbound"].append(href)
        self.set_nodes(links)

    def get_links(self, url):
        links = {"inbound": [], "outbound": []}
        r = requests.get(url)
        print(f'Getting links from {url}...')
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                if urlparse(href).netloc == urlparse(url).netloc:
                    links["inbound"].append(href)
                else:
                    links["outbound"].append(href)
        return links

    def create_mind_map(self):
        g = nx.DiGraph()
        root_url = urlparse(self.url).scheme + '://' + urlparse(self.url).netloc
        g.add_node(root_url)
        visited = set([root_url])
        queue = [root_url]
        while queue:
            current_url = queue.pop(0)
            for link in self.get_nodes().get(current_url, {}).get("outbound", []):
                if link not in visited:
                    visited.add(link)
                    queue.append(link)
                    g.add_node(link)
                    g.add_edge(current_url, link)
        pos = nx.spring_layout(g, seed=42)
        nx.draw(g, pos, with_labels=True, node_size=3000, font_size=10, arrows=False)
        plt.gcf().set_size_inches(18, 12)
        plt.savefig('mindmap.png', bbox_inches='tight')

aginic = WebsiteContentMap('https://aginic.com/')
links = aginic.get_links('https://aginic.com/blog/machine-learning/')
print(links)