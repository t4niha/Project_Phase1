# search_related_articles(headline, original_domain)
# print_related_articles(title, domain)

import requests
import spacy
from urllib.parse import urlparse

# List of 14 tested domains with usable HTML formats
allowed_domains = [
    'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
    'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
    'www.apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
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

def search_news_by_keywords(keywords):
    # List of allowed domains
    allowed_domains = [
        'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
        'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
        'www.apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
    ]
    
    # Array to store URLs
    url_list = []
    
    # NewsAPI endpoint and key
    NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
    api_url = 'https://newsapi.org/v2/everything'
    
    # Parameters for the API request
    params = {
        'apiKey': NEWS_API_KEY,
        'q': keywords,
        'sortBy': 'relevancy',
        'pageSize': 20,  # Fetch 20 articles to ensure we get enough from allowed domains
        'language': 'en'  # English articles only
    }
    
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            # Filter articles from allowed domains
            for article in articles:
                domain = urlparse(article['url']).netloc
                if domain in allowed_domains:
                    url_list.append(article['url'])
                    # Break if we have 5 URLs
                    if len(url_list) == 5:
                        break
                        
            return url_list[:5]  # Return up to 5 URLs
                
        else:
            print("Error: Could not fetch news articles.")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []
import requests
from urllib.parse import urlparse

def search_news_by_keywords2(keywords):
    # List of allowed domains
    allowed_domains = [
        'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
        'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
        'apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
    ]
    
    # Array to store article information
    articles_info = []
    
    # NewsAPI endpoint and key
    NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
    api_url = 'https://newsapi.org/v2/everything'
    
    # Parameters for the API request
    params = {
        'apiKey': NEWS_API_KEY,
        'q': keywords,
        'sortBy': 'relevancy',
        'pageSize': 20,  # Fetch 20 articles to ensure we get enough from allowed domains
        'language': 'en'  # English articles only
    }
    
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            # Filter articles from allowed domains
            for article in articles:
                domain = urlparse(article['url']).netloc
                if domain in allowed_domains:
                    article_info = {
                        'url': article['url'],
                        'title': article['title'],
                        'domain': domain
                    }
                    articles_info.append(article_info)
                    # Break if we have 5 articles
                    if len(articles_info) == 5:
                        break
                        
            return articles_info[:5]  # Return up to 5 articles
                
        else:
            print("Error: Could not fetch news articles.")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []

def find_related_articles(original_url):
    # List of allowed domains
    allowed_domains = [
        'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
        'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
        'www.apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
    ]
    
    # Excluded domains
    excluded_domains = [
        'www.nakedcapitalism.com', 'www.zerohedge.com', 'www.newsnow.co.uk', 'gizmodo.com', 
        'slashdot.org', 'www.drudge-report.com', 'www.buzzfeed.com', 'www.huffpost.com', 
        'en.wikipedia.org'
    ]
    
    # Extract domain and validate input URL
    input_domain = urlparse(original_url).netloc
    
    # Check if the input domain is allowed
    if input_domain not in allowed_domains:
        print(f"Error: The domain {input_domain} is not in the list of allowed domains.")
        return []
    
    # NewsAPI endpoint and key
    NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
    api_url = 'https://newsapi.org/v2/everything'
    
    try:
        # Fetch the original article to get its title for searching
        response = requests.get(original_url)
        response.raise_for_status()
        
        # Use BeautifulSoup to extract the title
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        original_title = soup.find('title').get_text().strip()
        
        # Parameters for API request
        params = {
            'apiKey': NEWS_API_KEY,
            'q': original_title,  # Search using the original article's title
            'sortBy': 'relevancy',
            'pageSize': 20,
            'language': 'en'
        }
        
        # Make the API request
        search_response = requests.get(api_url, params=params)
        search_response.raise_for_status()
        data = search_response.json()
        
        if search_response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            # Array to store related articles
            related_articles = []
            
            # Filter articles
            for article in articles:
                # Skip the original article
                if article['url'] == original_url:
                    continue
                
                # Get the article's domain
                domain = urlparse(article['url']).netloc
                
                # Check domain conditions
                if domain in allowed_domains:
                    related_article = {
                        'url': article['url'],
                        'title': article['title'],
                        'domain': domain,
                        'original_domain_match': domain == input_domain
                    }
                    related_articles.append(related_article)
                    
                    # Break if we have 5 articles
                    if len(related_articles) == 5:
                        break
            
            # Sort to prioritize articles from the same domain
            related_articles.sort(key=lambda x: x['original_domain_match'], reverse=True)
            
            return related_articles
        
        else:
            print("Error: Could not fetch related articles.")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    


def extract_keywords(sentence):
    """
    Extracts relevant keywords from a sentence for searching.
    
    Args:
        sentence (str): The input sentence.
        
    Returns:
        list: A list of keywords.
    """
    # Load the small English NLP model from SpaCy
    nlp = spacy.load("en_core_web_sm")
    
    # Process the sentence with SpaCy
    doc = nlp(sentence)
    
    # Define stop words and extract significant tokens
    keywords = [
        token.text.lower() for token in doc 
        if token.is_alpha and  # Include only alphabetic words
           not token.is_stop and  # Exclude stop words
           token.pos_ in {"NOUN", "PROPN", "VERB"}  # Focus on nouns, proper nouns, and verbs
    ]
    
    if len(keywords) <= 2:
        return ""
    
    # Extract only the middle words and join them
    middle_keywords = keywords[2:-2]  # Exclude the first and last keywords
    return " ".join(middle_keywords)


def refine_keywords(headline):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(headline)
    # Extract meaningful entities and nouns
    keywords = [token.text.lower() for token in doc if token.is_alpha and token.pos_ in {"NOUN", "PROPN"}]
    return " ".join(keywords)

def find_original_article(content):
    import re
    from collections import Counter
    
    # List of allowed domains
    allowed_domains = [
        'time.com', 'abcnews.go.com', 'edition.cnn.com', 'www.theguardian.com', 'www.nbcnews.com',
        'theconversation.com', 'www.bbc.com', 'www.dailymail.co.uk', 'www.cbsnews.com', 'www.thewrap.com',
        'apnews.com', 'www.aljazeera.com', 'www.usatoday.com', 'www.wired.com'
    ]
    
    # NewsAPI endpoint and key
    NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
    api_url = 'https://newsapi.org/v2/everything'
    
    # Clean and process the content
    def extract_key_phrases(text):
        # Remove non-alphanumeric characters
        text = re.sub(r'\W+', ' ', text)
        # Tokenize and get most common words
        words = text.lower().split()
        common_words = Counter(words).most_common(10)  # Adjust the number of key phrases as needed
        return [word for word, _ in common_words]
    
    # Extract key phrases from the content
    key_phrases = extract_key_phrases(content)
    query = " ".join(key_phrases)
    
    # Parameters for the API request
    params = {
        'apiKey': NEWS_API_KEY,
        'q': query,
        'sortBy': 'relevancy',
        'pageSize': 20,
        'language': 'en'
    }
    
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            # Filter articles from allowed domains and check content similarity
            for article in articles:
                domain = urlparse(article['url']).netloc
                if domain in allowed_domains:
                    # Check if the article content matches the original
                    if all(phrase in article['title'].lower() or article.get('description', '').lower() for phrase in key_phrases):
                        return {
                            'url': article['url'],
                            'title': article['title'],
                            'domain': domain
                        }
            
            print("Original article not found.")
            return None  # No matching article found
                
        else:
            print("Error: Could not fetch news articles.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
    
def fetch_original_article(keywords):
    """
    Fetch the original article based on the provided keywords (e.g., headline or content snippet).
    Returns the URL, domain, and title of the most relevant article.
    """
    # NewsAPI endpoint and key
    NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
    api_url = 'https://newsapi.org/v2/everything'
    
    # Parameters for the API request
    params = {
        'apiKey': NEWS_API_KEY,
        'q': keywords,       # Use keywords to search
        'sortBy': 'relevancy',
        'pageSize': 1,       # Fetch only the most relevant article
        'language': 'en'     # English articles only
    }
    
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            if articles:
                # Extract the first (most relevant) article
                article = articles[0]
                domain = urlparse(article['url']).netloc
                return {
                    'url': article['url'],
                    'title': article['title'],
                    'domain': domain
                }
            else:
                print("No articles found.")
                return None
                
        else:
            print("Error: Could not fetch the article.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def testAPI(query):
    """
    Test the NewsAPI by directly making a request with specified parameters.
    
    Parameters:
        api_key (str): Your NewsAPI key.
        query (str): The search query (headline or keywords).
        language (str): The language of the articles (default: 'en').
        page_size (int): Number of articles to fetch (default: 10).
    
    Returns:
        dict: The JSON response from the NewsAPI.
    """
    try:
        api_url = 'https://newsapi.org/v2/everything'
        NEWS_API_KEY = '1c9bf38bc975416bb58e54b6774da94e'
        params = {
            'apiKey':  NEWS_API_KEY,
            'q': query,
            'pageSize': 1,
            'language': 'en'
            
        }
        
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse and return the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API call: {e}")
        return {"error": str(e)}

