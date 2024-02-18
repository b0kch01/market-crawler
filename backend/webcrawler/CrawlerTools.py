from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time

def valid_url(url:str) -> bool:
    """returns whether this url is valid for search"""
    unnecessary_links = (
        'https://www.instagram.com',
        'https://www.google.com/search',
        'https://www.facebook.com/'
    )
    return url and not url.startswith(unnecessary_links)

def get_google_alert_links(search_key: str, browser) -> list[str]:
    """Given search key, returns a list of todays google alerts of the search_key"""
    google_alerts_url = 'https://www.google.com/alerts#1:0'

    browser.get(google_alerts_url)

    elem = browser.find_element(By.XPATH, "//input[@aria-label='Create an alert about...']")
    elem.send_keys(search_key)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'result'))
        # Google's search results are within an element with ID 'search'
    )

    links = []
    search_results = browser.find_elements(By.XPATH, "//li[@class='result']")

    for result in search_results:
        anchor_tags = result.find_elements(By.CSS_SELECTOR, 'a')
        for a in anchor_tags:
            url = a.get_attribute('href')
            if valid_url(url):
                links.append(url)

    return links
def make_google_search(search_query: str, browser, num_links=3):
    """makes a google search and returns the top 'num_links' links"""
    browser.get('https://www.google.com')
    assert 'Google' in browser.title

    # Find the Google search box and enter the search query
    elem = browser.find_element(By.NAME, 'q')  # Google's search box name is 'q'

    # Input search input
    elem.send_keys(search_query + Keys.RETURN)

    # Wait for search results to load
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
        # Google's search results are within an element with ID 'search'
    )

    # Collect URLs from search results
    links = []
    search_results = browser.find_elements(By.CSS_SELECTOR,
                                           '#search .g')  # Each result is within a div with class 'g'

    for result in search_results:
        anchor_tags = result.find_elements(By.CSS_SELECTOR, 'a')
        for a in anchor_tags:
            url = a.get_attribute('href')
            if valid_url(url):
                links.append(url)
    links = links[:num_links]

    return links
def scrape_page_text(url:str, browser) -> str:
    """Returns text from specified URL, pass browser in"""
    text=""
    try:
        # Navigate to the URL
        browser.get(url)

        # Wait for a specific element that indicates the page has dynamically loaded content
        # Adjust the CSS selector according to your needs
        wait = WebDriverWait(browser, 5)
        # wait.until(EC.visibility_of_element_located((By.ID, 'app')))

        # Wait for the page to completely render

        # Optional: wait a bit for surety (not the best practice, but works as a last resort)
        time.sleep(5)

        # Now that the page is loaded, retrieve the page source
        page_source = browser.page_source

        # Use Beautiful Soup to parse the HTML
        soup = BeautifulSoup(page_source, 'html.parser')
        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

    finally:
        # Make sure to close the browser
        pass

    return text

def get_all_tags_links_on_page(url:str, browser) -> list[str]:
    """returns all links on page of website -> great for smart navigation"""
    res = []
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 5)
        # wait.until(EC.visibility_of_element_located((By.ID, 'app')))

        # Wait for the page to completely render

        # Optional: wait a bit for surety (not the best practice, but works as a last resort)
        time.sleep(12)
        links = browser.find_elements(By.CSS_SELECTOR, 'a')
        print(links)
        for link in links:
            res.append({'label':link.text, 'link':link.get_attribute('href')})
    finally:
        pass

    return res;

def get_images(foodhall:str, browser)->list[str]:
    """given google search link, return photo images of food hall"""
    try:
        search_url = f'https://www.google.com/search?hl=en&tbm=isch&q={foodhall}'
        browser.get(search_url)
        # Wait for images to load
        time.sleep(2)  # Adjust sleep time as necessary

        # Find image elements - Adjust the selector if necessary
        images = browser.find_elements(By.CSS_SELECTOR, 'img')
        image_urls = []
        for image in images:
            # Get the src of the image
            src = image.get_attribute('src')
            if src and (src.endswith('.png') or src.endswith('.jpeg') or src.endswith('.jpg')):
                image_urls.append(src)
            if len(image_urls) == 10:
                break;

        return image_urls
    finally:
        pass


if __name__ == '__main__':
    browser = webdriver.Chrome()
    print(get_images('alton food hall',browser))