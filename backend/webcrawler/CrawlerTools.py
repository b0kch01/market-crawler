from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
import screeninfo
import threading

import os

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

import time
import json


def valid_url(url: str) -> bool:
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

    elem = browser.find_element(
        By.XPATH, "//input[@aria-label='Create an alert about...']")
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
    browser.get(f'https://www.google.com/search?q={search_query}')

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


def scrape_page_text(url: str, browser) -> str:
    """Returns text from specified URL, pass browser in"""
    text = ""
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
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

    finally:
        # Make sure to close the browser
        pass

    return text


def get_all_tags_links_on_page(url: str, browser) -> list[str]:
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
            res.append(
                {'label': link.text, 'link': link.get_attribute('href')})
    finally:
        pass

    return res


def get_images(foodhall: str, browser) -> list[str]:
    """given google search link, return photo images of food hall"""
    try:
        search_url = f'https://www.google.com/search?hl=en&tbm=isch&q={foodhall}'
        browser.get(search_url)
        # Wait for images to load
        time.sleep(2)  # Adjust sleep time as necessary

        # Find image elements - Adjust the selector if necessary
        images = browser.find_elements(By.CSS_SELECTOR, 'a > div > img[width]')
        image_urls = []
        for image in images:
            # Get the src of the image
            src = image.get_attribute('src')
            if src:
                image_urls.append({
                    "url": src,
                    "alt": image.get_attribute('alt')
                })

            if len(image_urls) == 10:
                break

        # return json string of image urls with key 'images'
        return json.dumps({"images": image_urls})
    finally:
        pass

def scrape_google_alert(browser, search_key="new food hall") -> list:
    """given a search key, return the list of new articles pertaining to search key"""
    google_alerts_url = 'https://www.google.com/alerts#1:0'
    browser.get(google_alerts_url)

    elem = browser.find_element(By.XPATH, "//input[@aria-label='Create an alert about...']") 
    elem.send_keys(search_key)

    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'result'))  # Google's search results are within an element with ID 'search'
        )

    links = []
    search_results = browser.find_elements(By.XPATH,"//li[@class='result']")

    for result in search_results:
            anchor_tags = result.find_elements(By.CSS_SELECTOR, 'a')
            for a in anchor_tags:
                url = a.get_attribute('href')
                if valid_url(url):
                    links.append(url)
    
    print(links)
    return links

def determine_food_halls_in_parallel(links):
        '''Returns objects of new halls to research '''
        res = []
        options = Options()
        options.page_load_strategy = 'eager'

        # Initialize browser instances
        browser1 = webdriver.Chrome(options=options)
        browser2 = webdriver.Chrome(options=options)
        browser3 = webdriver.Chrome(options=options)
        browser4 = webdriver.Chrome(options=options)

        # Set window sizes for a 1920x1080 resolution, adjust these values based on your actual screen resolution
        screen = screeninfo.get_monitors()[0]
        width = screen.width // 2
        height = screen.height // 2

        # Position the windows in a 4-quadrant layout
        # Top-Left
        browser1.set_window_position(0, 0)
        browser1.set_window_size(width, height)

        # Top-Right
        browser2.set_window_position(width, 0)
        browser2.set_window_size(width, height)

        # Bottom-Left
        browser3.set_window_position(0, height)
        browser3.set_window_size(width, height)

        # Bottom-Right
        browser4.set_window_position(width, height)
        browser4.set_window_size(width, height)

        # Define the tasks for each browser (quartering the total tasks)
        first_q = len(links) // 4
        second_q = 2 * first_q
        third_q = 3 * first_q

        links_to_research1 = links[:first_q]
        links_to_research2 = links[first_q:second_q]
        links_to_research3 = links[second_q:third_q]
        links_to_research4 = links[third_q:]

        # Create and start threads for each set of tasks
        thread1 = threading.Thread(
            target=determine_new_food_hall, args=(browser1, links_to_research1, res))
        thread2 = threading.Thread(
            target=determine_new_food_hall, args=(browser2, links_to_research2, res))
        thread3 = threading.Thread(
            target=determine_new_food_hall, args=(browser3, links_to_research3, res))
        thread4 = threading.Thread(
            target=determine_new_food_hall, args=(browser4, links_to_research4, res))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        # Wait for all threads to complete
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

        # Close browsers after completing tasks
        browser1.quit()
        browser2.quit()
        browser3.quit()
        browser4.quit()

        return res

def determine_new_food_hall(browser, new_food_hall_article_links, res_list):
    '''determines new food hall'''
    for link in new_food_hall_article_links:
        try:
            webcontent = scrape_page_text(link, browser)
            location_instruction = 'The aim of your market research is to find out the name of new food halls after reading an article. The article may or may not have relevant information to a new food hall, so analyze the text to see if a new food hall is opened.'
            prompt = f'Find out the name of the new food hall reading this article.' + \
                ' return the response as raw json: \'{"food_hall_name": "food_hall_name"}\' or \'{"data": null}\' if there are no new food hall.'
            res = gpt_request(location_instruction, prompt + webcontent)

            if '```json' in res:
                res = res[8: -3]

            json_res = json.loads(res)
            json_res['source'] = link
            
            res_list.append(json_res)
        except:
            print('uh oh')

def gpt_request(gpt_instruction: str, user_prompt: str):
        open_ai_key = os.getenv('GPT_API_KEY')
        gpt_client = OpenAI(api_key=open_ai_key)

        GPT_INSTRUCTIONS = gpt_instruction
        user_prompt = user_prompt

        response = gpt_client.chat.completions.create(
            model="gpt-3.5-turbo",
            seed=42,
            temperature=0.3,
            messages=[
                {"role": "system", "content": GPT_INSTRUCTIONS},
                {"role": "user", "content": user_prompt}
            ]
        )
        payload = response.choices[0].message.content
        return payload

if __name__ == '__main__':
    browser = webdriver.Chrome()
    print(scrape_google_alert(browser))
