import re  # For matching archive URL patterns
import requests  # To send HTTP requests
from bs4 import BeautifulSoup as bs  # To parse HTML
from collections import Counter  # To count article frequencies per author
import time  # To add delay between requests
import random  # To generate random delay durations
import csv  # For writing CSV files


# This function gets all archive page links from the main archives page.
def get_archive_links(main_url):
    headers = {
        # Standard user agent header to mimic a web browser
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/91.0.4472.124 Safari/537.36')
    }

    # Request the main archives page
    response = requests.get(main_url, headers=headers)
    response.raise_for_status()  # Stop if there's an error with the request

    # Parse the HTML content
    soup = bs(response.content, 'html.parser')

    # Set to store unique archive links
    links = set()
    # Regex pattern to match URLs like "/archives/YYYY/MM"
    pattern = re.compile(r'^/archives/\d{4}/\d{2}/?$')

    # Loop over all anchor tags to find matching links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if pattern.match(href):
            # Build the full URL and add it to our set
            full_url = "https://fountainmagazine.com" + href
            links.add(full_url)
    return list(links)


# This function extracts author names from an archive page.
def extract_authors(url):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/91.0.4472.124 Safari/537.36')
    }

    # Request the archive page
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse the page's HTML
    soup = bs(response.content, 'html.parser')
    # Find all div elements that contain the author information
    author_divs = soup.find_all('div', class_='w357ui-display-inline-block w357ui-margin-right ma-author')

    authors = []
    # Loop through each found element to extract the author text
    for div in author_divs:
        # Remove "By" from the text and strip extra spaces
        text = div.get_text(strip=True).replace("By", "").strip()
        authors.append(text)
    return authors


def main():
    # URL of the main archives page
    main_url = "https://fountainmagazine.com/archives"
    # Get a list of archive page links
    archive_links = get_archive_links(main_url)
    print("Archive pages found:")
    for link in archive_links:
        print(link)

    all_authors = []  # List to store authors from all pages

    # Loop over each archive page and extract authors
    for url in archive_links:
        print("\nProcessing page:", url)
        authors = extract_authors(url)
        print("Found authors:", authors)
        all_authors.extend(authors)
        # Delay randomly between 1 to 3 seconds to be polite to the server
        time.sleep(random.uniform(1, 3))

    # Write all authors to a CSV file with one column
    with open("authors.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for author in all_authors:
            writer.writerow([author])
    print("\nAuthors written to authors.csv")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()