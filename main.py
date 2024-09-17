# get_option()

from article_processor import print_article, clean_title
from news_scraping import print_related_articles
import keyboard


def get_option():
    print("_____________________________________________")
    print("1. Enter news article url")
    print("2. Manually enter news article")
    print("3. Search for news article")
    print("\nEnter Option: ")

    # Capture key press by user
    option = keyboard.read_event(suppress=True).name

    # Keep taking user input until 1/2/3 entered
    while option != '1' and option != '2' and option != '3':
        option = keyboard.read_event(suppress=True).name

    print(f"[Option {option} selected]")
    print("_____________________________________________")

    return option


def main():
    print("\n NEWS BIAS DETECTION USING MACHINE LEARNING")
    print("(Akif Zahin | Taniha Tripura | Ekfat Nowshin)")

    option = get_option()

    if option == '1':
        # Get URL input from the user
        url = input("\nEnter the URL of the news article: ")

        # Retrieve and print article data
        title, content = print_article(url)

    elif option == '2':
        # Prompt user to manually enter article
        print("\nPlease enter the title and content of the article.")
        title = input("\nTITLE: ")
        content = input("\nARTICLE CONTENT: ")
        url = ''

    elif option == '3':
        # Prompt user to enter search prompt
        title = input("\nEnter the search query: ")
        content = ''
        url = ''

    else:
        print("\nInput Error")
        return

    # TODO: THE NLP AND ML STUFF GOES HERE: analyze original & related articles' content

    # Print list of related articles using NewsAPI
    cleaned_title = clean_title(title)
    print_related_articles(cleaned_title, url)


if __name__ == "__main__":
    main()
