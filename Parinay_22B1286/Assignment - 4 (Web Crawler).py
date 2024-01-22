import re
from datetime import datetime
from urllib.parse import urljoin

import matplotlib.pyplot as plt
import networkx as nx
import requests
from bs4 import BeautifulSoup
from termcolor import colored


class WebCrawler:
    def __init__(self, url, max_depth):
        self.url = url
        self.max_depth = max_depth
        self.subdomains = set()
        self.links = set()
        self.jsfiles = set()
        self.graph = nx.Graph()

    def start_crawling(self):
        self.crawl(self.url, depth=1)

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            soup = BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as err:
            print(f"[-] An error occurred: {err}")
            return

        for link in soup.find_all("a"):
            link_text = link.get("href")
            if link_text:
                full_link = urljoin(url, link_text)
                if full_link != url and full_link not in self.links:
                    self.links.add(full_link)
                    self.graph.add_edge(url, full_link)
                    self.crawl(full_link, depth + 1)

    def visualize_structure(self):
        pos = nx.spring_layout(self.graph, seed=42)  # Use seed for reproducibility
        plt.figure(
            figsize=(12, 10), facecolor="lightyellow"
        )  # Set facecolor for colorful background

        # Customize node colors, sizes, and labels
        nx.draw_networkx_nodes(
            self.graph, pos, node_size=300, node_color="lightcoral", label="URLs"
        )
        nx.draw_networkx_labels(
            self.graph, pos, font_size=8, font_color="black", font_family="sans-serif"
        )

        # Customize edge colors and width
        nx.draw_networkx_edges(self.graph, pos, edge_color="darkcyan", width=1.0)

        # Add title and legend
        plt.title("Website Structure Visualization", fontsize=16, color="purple")
        plt.legend()

        plt.axis("off")
        plt.show()

    def print_banner(self):
        print("-" * 80)
        print(
            colored(
                f"Recursive Web Crawler starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                "cyan",
                attrs=["bold"],
            )
        )
        print("-" * 80)
        print(f"[*] URL".ljust(20, " "), ":", self.url)
        print(f"[*] Max Depth".ljust(20, " "), ":", self.max_depth)
        print("-" * 80)

    def print_results(self):
        if self.links:
            for link in self.links:
                print(f"[+] Links : {link}")

        print()


def get_user_input():
    url = input("Enter the URL: ")
    depth = int(input("Enter the recursion depth: "))
    return url, depth


if __name__ == "__main__":
    url, depth = get_user_input()
    web_crawler = WebCrawler(url, depth)
    web_crawler.print_banner()
    web_crawler.start_crawling()
    web_crawler.print_results()

    # Visualize the website structure
    web_crawler.visualize_structure()
