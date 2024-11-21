from article_processor import fetch_article,fetch_article2,print_article, clean_title
from news_scraping import fetch_original_article,testAPI,print_related_articles, search_related_articles,search_news_by_keywords, search_news_by_keywords2,find_related_articles,extract_keywords,refine_keywords,find_original_article
from prediction import makePrediction
from functions import urlButton1,urlButton2,urlButton3


def main():
    url = "https://www.wired.com/story/election-violence-is-already-here/"
    # related = find_related_articles(url)

    # # Detailed exploration
    # for article in related:
    #     print(f"Title: {article['title']}")
    #     print(f"Domain: {article['domain']}")
    #     print(f"Same Domain: {article['original_domain_match']}")

    # print(urlButton3(url))
    # title1 = urlButton3(url)  # Fetch up to 5 related articles
    # title2 = clean_title(title1)
    # print(title2)
    # title3 = extract_keywords(title2)
    # print(title3)
    # articles = urlButton2(title3)
    # print(articles)
    # # print(urlButton2("Donald Trump"))
    
    # keywords = "live president elect responds laken riley migrant killer verdict "
    # ogTitle = urlButton3(url)
    # print(f"Original Keywords: {ogTitle}")  

    # ogTitle = refine_keywords(ogTitle)  
    # print(f"Original Keywords: {ogTitle}")  
    # articles = search_news_by_keywords2(ogTitle)
    # print(articles)

    # content = "pathway to a national ID . I don ’ t think that government should have the awesome power of monitoring the legal activities of American citizens . That is not a proper role of the federal government — or any level of government , for that matter . I am opposed to immigration reform that contains the photo tool that is contained in the Interior Enforcement and Employment Verification System title of the bill . In the name of preventing the “ unlawful employment of aliens , ” the Senate legislation has a provision that “ enables employers to match the photo on a covered identify document provided to the employer to a photo maintained by the U.S . Citizenship and Immigration Services database. ” This , too , is troubling . This sounds like a national picture database of all citizens , where the states house the picture and the Department of Homeland Security is the clearinghouse for worker verification . A national database of citizens raises the question : What activities will require someone to present their papers ? A national ID allows more power to gravitate to Washington and a greater likelihood that power will be abused . I will fight to remove the photo tool from this legislation because I think it will become a national ID . We already know the federal government is rife with false positives on the no-fly list and the National Instant Check system for gun buyers . Why would we be foolish enough to think that a massive database of all citizens would not have the same problems on a grander scale ? We have a Second Amendment that must be protected . We also have a Fourth Amendment that must be protected . Citizenship means that the government is supposed to protect our rights , not take them away . We must have stronger borders , but there ’ s no reason we can ’ t have better security while respecting constitutional limits and liberties . In the past week , we have witnessed examples of the Obama administration spying on the media and Internal Revenue Service discrimination against Tea Party free speech . People around the world always have dreamed of emigrating to America , the Land of the Free . It is our job to make sure our country stays that way . Sen. Rand Paul , Kentucky Republican , is a member of the Senate Foreign Relations and Homeland Security committees ."    
    # result = find_original_article(content)
    # if result:
    #     print(f"Original Article Found: {result}")
    # else:
    #     print("No matching article found.")

    
    # content = refine_keywords(content)
    # print(content)
    # print(urlButton2(content))
    
    # url = "https://www.wired.com/story/election-violence-is-already-here/"
    # article = fetch_original_article(headline)
    # print(article)
    headline = "India’s envoy to Canada rejects involvement in Sikh activist’s killing"
    # headline = refine_keywords(headline)
    headline = extract_keywords(headline)
    print(headline)
    print(testAPI(headline))
    

    
    

if __name__ == "__main__":
    main()
