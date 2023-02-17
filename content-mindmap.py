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
