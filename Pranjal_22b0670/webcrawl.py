import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import matplotlib.pyplot as plt
import time

def download_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error downloading page: {e}")
        return None

def extract_links(html, base_url):
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        absolute_url = urljoin(base_url, link)
        links.append(absolute_url)
    return links

def print_unique_domains(links):
    domains = set(urlparse(link).netloc for link in links)
    print("Unique Domains:")
    for domain in domains:
        print(domain)

def crawl(url, depth=3, link_counts=None):
    if depth == 0:
        return
    print(f"Crawling: {url}")

    html = download_page(url)
    if html is not None:
        links = extract_links(html, url)

        # Update link_counts dictionary
        if link_counts is not None:
            link_counts[depth] = len(links)

        # Print unique domains
        print_unique_domains(links)

        for link in links:
            # Introduce a delay of 1 second between requests
            time.sleep(1)
            crawl(link, depth - 1, link_counts)

def plot_links(link_counts):
    depths = list(link_counts.keys())
    counts = list(link_counts.values())

    plt.figure(figsize=(8, 6))
    plt.bar(depths, counts, color='blue')
    plt.xlabel('Depth')
    plt.ylabel('Number of Links')
    plt.title('Number of Links at Each Recursive Depth')
    plt.show()

if __name__ == "__main__":
    # Test the crawler with a starting URL
    start_url = "https://www.teamshunya.com/"

    # Dictionary to store link counts at each depth
    link_counts = {}

    # Crawl and collect link counts
    crawl(start_url, link_counts=link_counts)

    # Plot the results
    plot_links(link_counts)
