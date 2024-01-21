import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return []

def recursive_crawler(url, depth, visited=set()):
    if depth == 0 or url in visited:
        return []

    print(f"Crawling: {url}")
    visited.add(url)
    links = get_links(url)

    for link in links:
        recursive_crawler(link, depth - 1, visited)

    return visited

# Example usage
starting_url = "https://example.com"
crawl_depth = 2
result = recursive_crawler(starting_url, crawl_depth)

print(f"Visited {len(result)} unique links.")