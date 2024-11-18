# search_related_articles(headline, original_domain)
# print_related_articles(title, domain)

import requests
from urllib.parse import urlparse

# List of 14 tested domains with usable HTML formats
allowed_domains = [
    'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
    'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
    'apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
]
# Blacklisted domains (link aggregators, content farms, etc.)
excluded_domains = ['www.nakedcapitalism.com', 'www.zerohedge.com', 'www.newsnow.co.uk', 'gizmodo.com', 'slashdot.org',
                    'www.drudge-report.com', 'www.buzzfeed.com', 'www.huffpost.com', 'en.wikipedia.org']

# Key needed to access NewsAPI and authenticate requests (using Taniha's account)
NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'


# Search for related articles with NewsAPI using retrieved title
def search_related_articles(headline, original_url):
    # Endpoint for NewsAPI's 'everything' search
    api_url = 'https://newsapi.org/v2/everything'
    # Parameters for API request
    params = {
        'apiKey': NEWS_API_KEY,
        'q': headline,
        'sortBy': 'relevancy',
        'pageSize': 20  # Return 15 articles to be filtered, then top 5 will be printed
    }

    # Send HTTP GET request to NewsAPI endpoint with parameters, returns object containing JSON response from server
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Checks response for HTTP errors
    data = response.json()  # Decode JSON response received from web server into Python dictionary

    if response.status_code == 200 and data.get('status') == 'ok':  # Successful HTTP request and valid response
        articles = data.get('articles', [])  # Retrieve list of articles (empty list if none)

        # Two sets of articles (one from allowed domains, another from any except the excluded domains)
        filtered_articles = []
        extra_articles = []
        for article in articles:
            if urlparse(article['url']).netloc in allowed_domains and article['url'] != original_url:
                filtered_articles.append(article)
            elif ((urlparse(article['url']).netloc not in allowed_domains) and
                  (urlparse(article['url']).netloc not in excluded_domains)):
                extra_articles.append(article)

        return filtered_articles, extra_articles
    else:
        return []


# Print list of related articles
def print_related_articles(title, original_url):
    print(f"\nSEARCH PROMPT: {title}")

    # Retrieve lists of related articles
    filtered_articles, extra_articles = search_related_articles(title, original_url)

    if filtered_articles:
        print("\nFILTERED ARTICLES:\n")
        for article in filtered_articles[:5]:
            print(f"- {article['title']} ({article['source']['name']})")
            print(f"  URL: {article['url']}")
            # TODO: Call function to check article bias
            print()
    if extra_articles:
        print("\nEXTRA ARTICLES:\n")
        for article in extra_articles[:5]:
            print(f"- {article['title']} ({article['source']['name']})")
            print(f"  URL: {article['url']}")
            print()
    else:
        print("No related articles found.")
