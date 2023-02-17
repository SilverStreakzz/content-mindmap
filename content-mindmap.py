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
        links = {}
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Write code here to create a dictionary of nodes, where each node is a url and the value is a dictionary of inbound and outbound links

        self.set_nodes(links)

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
