import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from housekeeping import *
from domaingetter import *

def get_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    return []

def crawl(url, depth, visited, file_name):
    if depth == 0 or url in visited:
        return

    print(f"Crawling: {url}")

    links = get_links(url)
    visited.add(url)

    for link in links:
        crawl(link, depth - 1, visited, file_name)

    set_to_file(visited, file_name)

if __name__ == "__main__":
    starting_url = input("Enter the starting URL: ")
    file_name = get_domain_name(starting_url) + ' links'
    make_folder(file_name)
    create_data_files(file_name)
    max_depth = int(input("Enter the maximum depth: "))

    
    visited_urls = set()
    
    crawl(starting_url, max_depth, visited_urls, file_name)
