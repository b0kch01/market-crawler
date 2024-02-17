from CrawlerTools import scrape_page_text
from CrawlerTools import get_google_alert_links
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()

    text = scrape_page_text('https://github.com/Jomango2003', browser)
    print(text)

    new_links = get_google_alert_links('new food hall', browser)
    print(new_links, browser)
    # use surrounding area data/ primary demographics / closed stores
    # use this data to make educated decisions on to build something or not