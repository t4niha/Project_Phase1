# clean_title(title)
# fetch_article(url)
# print_article(url)

import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from news_scraping import allowed_domains

# List of 6 randomly generated User-Agent headers (to bypass User-Agent Blocking)
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/92.0.4515.107 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edg/91.0.864.48'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) OPR/77.0.4054.172'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0'
]


# Exception class for unsupported domains
class UnsupportedDomainError(Exception):
    pass


# Clean retrieved title to optimize for future NewsAPI search
def clean_title(title):
    delimiters = ['- ', '|', ':']

    # Split title at first occurrence of '- ', '|', ':'
    for delimiter in delimiters:
        index = title.find(delimiter)
        if index != -1:
            title = title[:index].strip()

    return title.lower()


# Retrieve title and article text from given URL
def fetch_article(url):
    # Randomly select a User-Agent string from the list
    header = {
        'User-Agent': random.choice(user_agents)
    }
    # Send HTTP GET request to URL with the selected User-Agent, returns object containing server response
    response = requests.get(url, headers=header)
    response.raise_for_status()  # Checks response for HTTP errors

    if response.status_code == 200:  # Successful HTTP request
        # Parsing: analyze HTML code of webpage and extract info
        parsed_content = BeautifulSoup(response.content, 'html.parser')

        # Extract title of the article (at first <title> tag)
        title = parsed_content.find('title').get_text()

        # Extract text contents of the article (from all <p> paragraph tags)
        content = ''
        paragraphs = parsed_content.find_all('p')  # List of objects for each <p> tag found
        for paragraph in paragraphs:
            content += paragraph.get_text() + '\n'  # Append text extracted from each object

        return title.strip(), content.strip()
    else:
        return None, 'Failed to retrieve the article'


# Print title and article, handle missing data
def print_article(url):
    # Extract domain from the URL
    domain = urlparse(url).netloc
    if domain == '':
        domain = url

    try:
        # Check if the domain is allowed
        if domain not in allowed_domains:
            raise UnsupportedDomainError(f"'{domain}' domain format not supported.")

        # Fetch article title and content from the URL
        title, content = fetch_article(url)

        # TODO: Don't print article content (WHEN TESTING DONE) OR print cleaned_content from clean_content(content)
        # Print domain, title, and article content (or prompt user for manual input if unavailable)
        print(f"\nSOURCE: {domain}")
        if title and content:
            print(f"\nTITLE: {title}")
            print("\nARTICLE CONTENT:\n\n", content)
        elif content:
            print("\nUnable to retrieve the title of the article. Please enter manually.")
            title = input("TITLE: ")
            print("\nARTICLE CONTENT:\n\n", content)
        elif title:
            print(f"\nTITLE: {title}")
            print("\nUnable to retrieve the content of the article. Please enter manually.")
            content = input("ARTICLE CONTENT: ")
        else:
            print("\nUnable to retrieve the title and content of the article. Please enter manually.")
            title = input("TITLE: ")
            content = input("ARTICLE CONTENT: ")

    except (requests.RequestException, UnsupportedDomainError) as e:
        print(f"\nError: {e}")

        # Prompt user for manual input if there's a request exception
        print("Unable to retrieve the title and content of the article. Please enter manually.")
        title = input("\nTITLE: ")
        content = input("\nARTICLE CONTENT: ")

    return title, content
