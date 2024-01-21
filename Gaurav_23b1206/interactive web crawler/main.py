import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebCrawler:
    def __init__(self, url, max_depth):
        self.url = url
        self.max_depth = max_depth
        self.links = set()     

    def start_crawling(self):
        self.crawl(self.url, depth=1)

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as err:
            print(f"[-] An error occurred: {err}")
            return

        for link in soup.find_all('a'):
            link_text = link.get('href')
            if link_text:
              
                full_link = urljoin(url, link_text)
                if full_link != url and full_link not in self.links:
                    self.links.add(full_link)
                    self.crawl(full_link, depth + 1)

    def print_results(self):
  
        if self.links:
            for link in self.links:
                print(f"[+] Links : {link}")

        print()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', help="Specify the URL, provide it along http/https", required=True)
    parser.add_argument('-d', '--depth', dest='depth', type=int, default=1, help="Specify the recursion depth limit")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    web_crawler = WebCrawler(args.url, args.depth)
    web_crawler.start_crawling()
    web_crawler.print_results()
