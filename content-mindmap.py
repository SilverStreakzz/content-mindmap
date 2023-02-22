import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import networkx as nx
import matplotlib.pyplot as plt


class WebsiteMap:
    """
    This class is used to generate a mindmap of website content, based on a url.
    """
    def __init__(self, url):
        self.url = url
        self.nodes = {}
        self.create_nodes()
    
    def create_links(self, url):
        """ Create links.
        
        Creates a list of links for the current url.
        """
        links = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                link_domain = urlparse(href).netloc
                if link_domain == urlparse(url).netloc:
                    links.append(href)
        return links
    
    def filter_links(self, links):
        """ Filter links.
        
        Filters the list of links to remove any that are not a part of the main website url.
        """
        url = get_url()
        filtered_links = []
        for link in links:
            if link.startswith(url):
                filtered_links.append(link)

        return filtered_links
    
    def create_link_dict(self):
        """ Create link dictionary.

        Creates a dictionary of links, where each key is a url and the value is a list of links.

        Sample output:
            {
                "https://aginic.com/blog/": 
                [
                    "https://aginic.com/blog/what-is-a-mind-map/",
                    "https://aginic.com/blog/analytics/",
                    "https://aginic.com/blog/machine-learning/"
                    ],
                "https://aginic.com/blog/what-is-a-mind-map/":
                [
                    "https://aginic.com/blog/",
                    ],
                "https://aginic.com/blog/analytics/": [],
                "https://aginic.com/blog/machine-learning/": []
                }
        """
        url = self.get_url()
        links = self.create_links(url)
        link_dict = {}
        for link in links:
            link_dict[link] = self.create_links(link)
        
        return link_dict

    def create_nodes(self):
        """ Create nodes.

        Creates a dictionary of nodes, where each node is a url and the value is a dictionary of inbound and outbound links.
        This dictionary is then set to self.nodes.  

        Sample output:
            {
                "https://aginic.com/blog/": {
                    "inbound": ["https://aginic.com/blog/what-is-a-mind-map/"],
                    "outbound": ["https://aginic.com/blog/what-is-a-mind-map/", "https://aginic.com/blog/what-is-a-mind-map/"]
                },
                "https://aginic.com/blog/what-is-a-mind-map/": {
                    "inbound": ["https://aginic.com/blog/"],
                    "outbound": ["https://aginic.com/blog/"]
                }
            }
        """
        link_dict = self.create_link_dict()
        node_dict = {}
        for key, value in link_dict.items():
            node_dict[key] = {
                "inbound": [],
                "outbound": value
            }
        for key, value in link_dict.items():
            if key in node_dict:


        self.set_nodes(nodes)

    def get_nodes(self) -> dict:
        return self.nodes

    def set_nodes(self, nodes: dict) -> None:
        self.nodes = nodes

    def get_url(self):
        return self.url

    def get_inbound_links(self, node):
        """ Get inbound links for a node (webpage)."""
        pass

    def get_outbound_links(self, node):
        """ Get outbound links for a node (webpage)."""
        pass

    def create_mind_map(self):
        """ Create a mindmap of the website content, using its nodes."""
        pass


aginic = WebsiteMap('https://aginic.com')
nodes = aginic.get_nodes()
print(nodes)
