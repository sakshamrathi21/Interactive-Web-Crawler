# Customization - Displaying progress rate, measured in iterations per second, where an iteration generally corresponds to reading a page
# Also showing the links according to the recursion depth
import re
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from termcolor import colored
from tqdm import tqdm


class WebCrawler:
    def __init__(self, url, max_depth):
        self.url = url
        self.max_depth = max_depth
        self.subdomains = set()
        self.links = {}  # Store links in a dictionary based on recursion depth
        self.jsfiles = set()

    def start_crawling(self):
        with tqdm(total=self.max_depth, desc="Crawling Progress") as pbar:
            self.crawl(self.url, depth=1, pbar=pbar)

    def crawl(self, url, depth, pbar):
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
                if full_link != url and full_link not in self.links.get(depth, set()):
                    if depth not in self.links:
                        self.links[depth] = set()
                    self.links[depth].add(full_link)
                    self.crawl(full_link, depth + 1, pbar)

        pbar.update(1)

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
        for depth, links in self.links.items():
            print(f"Recursion Depth {depth}:")
            for link in links:
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
