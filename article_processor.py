
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
    
def fetch_article2(url):
    # List of allowed domains
        allowed_domains = [
            'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
            'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
            'www.apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
        ]
        
        # List of excluded domains
        excluded_domains = [
            'www.nakedcapitalism.com', 'www.zerohedge.com', 'www.newsnow.co.uk', 'gizmodo.com', 
            'slashdot.org', 'www.drudge-report.com', 'www.buzzfeed.com', 'www.huffpost.com', 
            'en.wikipedia.org'
        ]

        # Extract domain from URL
        domain = urlparse(url).netloc

        # Check if domain is allowed
        if domain not in allowed_domains:
            if domain in excluded_domains:
                return None, 'This domain is blocked due to reliability concerns.'
            else:
                return None, 'This domain is not in our list of trusted news sources.'

        try:
            # Your list of user agents (assuming it's defined elsewhere)
            header = {
                'User-Agent': random.choice(user_agents)
            }

            # Send HTTP GET request
            response = requests.get(url, headers=header, timeout=10)  # Added timeout
            response.raise_for_status()

            if response.status_code == 200:
                # Parse the content
                parsed_content = BeautifulSoup(response.content, 'html.parser')
                
                # Extract title
                title_tag = parsed_content.find('title')
                if not title_tag:
                    return None, 'Could not find article title'
                title = title_tag.get_text()

                # Extract content
                content = ''
                paragraphs = parsed_content.find_all('p')
                if not paragraphs:
                    return None, 'Could not find article content'
                
                for paragraph in paragraphs:
                    paragraph_text = paragraph.get_text().strip()
                    if paragraph_text:  # Only add non-empty paragraphs
                        content += paragraph_text + '\n\n'

                return {
                     title.strip(), content.strip(),
                    
                }
            else:
                return None, f'Failed to retrieve article: HTTP {response.status_code}'

        except requests.Timeout:
            return None, 'Request timed out. The server took too long to respond.'
        except requests.RequestException as e:
            return None, f'Failed to retrieve article: {str(e)}'
        except Exception as e:
            return None, f'An unexpected error occurred: {str(e)}'


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
