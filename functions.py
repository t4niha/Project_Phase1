from prediction import makePrediction
from article_processor import clean_title,fetch_article,print_article
from news_scraping import fetch_original_article,search_related_articles,print_related_articles,search_news_by_keywords,search_news_by_keywords2,extract_keywords,find_related_articles,refine_keywords

def urlButton1(url):
    title,content = fetch_article(url)
    biasValue = makePrediction(content)
    return biasValue

def urlButton2(keywords):
    urlList = search_news_by_keywords2(keywords)
    return urlList
def urlButton3(url):
    title,content = fetch_article(url)
    title1 = clean_title(title)
    return title1    
