from CrawlerTools import make_google_search
from CrawlerTools import scrape_page_text
from selenium import webdriver
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import threading
import tkinter


load_dotenv()
open_ai_key = os.getenv('GPT_API_KEY')
client = OpenAI(api_key=open_ai_key)

# Use AI to click and navigate within that website, AI -> use for smart navigation

# to get info: look through website text info
# then look through html components
# then navigate through website
# to get info: look through website text info
# then look through html components


def gpt_request(gpt_instruction: str, user_prompt: str):
    """return a list of names of relevant halls"""
    GPT_INSTRUCTIONS = gpt_instruction
    user_prompt = user_prompt

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": GPT_INSTRUCTIONS},
            {"role": "user", "content": user_prompt}
        ]
    )
    payload = response.choices[0].message.content
    return payload

# Research functions


def research_in_depth(food_hall, topic, browser):
    """returns data about your topic: square footage, bands that played at the place, etc"""
    gpt_instruction = 'gpt generated instruction'
    pass


def get_location(food_hall: str, browser):  # google maps API
    """returns location of food hall"""
    res = None
    location_instruction = "You are a market researcher and you are helping me find information about certain food halls."
    prompt = f'Given this text content, determine the location of the food hall "{food_hall}"'+'. return the response as raw json: {"city": "CityName", "state": "StateCode"}'
    google_link = make_google_search(f'{food_hall} location', browser, 1)[0]
    try:
        webcontent = scrape_page_text(google_link, browser)
        res = gpt_request(location_instruction, prompt + webcontent)
    except:
        print('get_locations went wrong')

    return res


def get_square_footage(food_hall: str, browser):
    """returns get_square_footage of food hall"""
    res = None
    location_instruction = "You are a market researcher and you are helping me find information about certain food halls."
    prompt = f'Given this text content, determine the square footage of "{food_hall}"'+ '. return the response as raw json: {"square_footage": 10000} or {"square_footage": null} if data is unavailable.'

    google_link = make_google_search(
        f'{food_hall} square footage', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(location_instruction, prompt + webcontent)
    return res


def get_number_of_food_stalls(food_hall: str, browser):
    """returns number of food, bar, and retail stalls of food hall"""
    location_instruction = "You are a market researcher and you are helping me find information about certain food halls."
    prompt = f'Given this text content, determine the number of food stalls, bar stalls, and retail stalls in "{food_hall}"'+'. return the response as raw json: {"food": 3, "bars": 4, "retail": 3} or {"data": null} if information is not available.'

    google_link = make_google_search(
        f'{food_hall} number of food stalls', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(location_instruction, prompt + webcontent)
    return res

# GPT Generated all below... this is what we want to do with the universal scraper...


def get_types_of_food_stalls(food_hall: str, browser):
    """Returns types of food stalls in food hall"""
    instruction = "You are a market researcher and you are helping me find information about the types of food stalls in certain food halls."
    prompt = f'Given this text content, list the types of food stalls available in "{food_hall}"'+'. return the response as raw json: {"types_of_food_stalls": ["Mexican", "Italian", "Japanese"]} or {"types_of_food_stalls": null} if no data is found.'

    google_link = make_google_search(
        f'{food_hall} types of food stalls', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_demographic(food_hall: str, browser):
    """Returns demographic information of the area surrounding the food hall."""
    instruction = "You are a market researcher and you are tasked with gathering demographic information about the area surrounding a specific food hall."
    prompt = f'Analyze this text content to provide demographic information of the area surrounding "{food_hall}"'+'. return the response as raw json: {"population_density": "100/sq.miles", "median_income": "10000", "age_distribution": {"0-10": "10%", "11-24": "30%"}} or {"data": null} if specifics are unavailable.'

    google_link = make_google_search(
        f'{food_hall} area demographics', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_local_area_composition(food_hall: str, browser):
    """Returns information on the local area composition around the food hall."""
    instruction = "You are a market researcher and your objective is to understand the composition of the area surrounding a food hall."
    prompt = f'Evaluate the text content to describe the area composition around "{food_hall}"' + '. return the response as raw json: {"composition": ["office", "retail", "residential"]} or {"composition": null} if data is not available.'

    google_link = make_google_search(
        f'{food_hall} surrounding area composition', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_public_transport(food_hall: str, browser):
    """Returns public transport options available near the food hall."""
    instruction = "You are a market researcher, aiming to find out about public transport options available near a food hall."
    prompt = f'Summarize information about nearby public transport for "{food_hall}"'+'. return the response as raw json: {"public_transport": ["bus", "train", "bike"]} or {"public_transport": null} if information is scarce.'

    google_link = make_google_search(
        f'{food_hall} public transport options', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_parking_availability(food_hall: str, browser):
    """Returns parking availability information for the food hall."""
    instruction = "You are a market researcher focusing on parking availability for a particular food hall."
    prompt = f'Provide details on parking at "{food_hall}".'+' return the response as raw json: {"parking_spots": 1000, "parking_fees": "$5/hr", "peak_time_availability": "10:00am"} or {"data": null} if unavailable.'

    google_link = make_google_search(
        f'{food_hall} parking availability', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_foot_traffic_estimates(food_hall: str, browser):
    """Returns foot traffic estimates near the food hall."""
    instruction = "As a market researcher, your task is to estimate the foot traffic around a specific food hall."
    prompt = f'Determine the average foot traffic near "{food_hall}".'+' return the response as raw json: {"foot_traffic": "100/hr"} or {"foot_traffic": "1000/day"} or {"data": null} if estimates are not directly available.'

    google_link = make_google_search(
        f'{food_hall} foot traffic estimates', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_annual_visitor_count(food_hall: str, browser):
    """Returns the annual visitor count of the food hall."""
    instruction = "You are tasked with finding the annual visitor count for a food hall as part of a market research project."
    prompt = f'Extract information on annual visitor count for "{food_hall}"'+'. return the response as raw json: {"annual_visitor_count": 1000000} or {"data": null} if no specific numbers are found.'

    google_link = make_google_search(
        f'{food_hall} annual visitor count', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_lease_rates(food_hall: str, browser):
    """Returns lease rates for the food hall."""
    instruction = "Your objective as a market researcher is to determine the lease rates for spaces within a specific food hall."
    prompt = f'Provide the average lease rate for spaces within "{food_hall}".'+' return the response as raw json: {"lease_rates": "$800/sq.ft"} or {"data": null} if precise rates are not available.'

    google_link = make_google_search(f'{food_hall} lease rates', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_occupancy_rate(food_hall: str, browser):
    """Returns the occupancy rate of the food hall."""
    instruction = "As a market researcher, it's your job to find out the occupancy rate of a given food hall."
    prompt = f'Analyze to provide the occupancy rate for "{food_hall}".'+' return the response as raw json: {"occupancy_rate": "82%"} or {"data": null} if direct data is unavailable.'

    google_link = make_google_search(
        f'{food_hall} occupancy rate', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_year_established(food_hall: str, browser):
    """Returns the year the food hall was established."""
    instruction = "Your role as a market researcher involves finding out when a food hall was first established."
    prompt = f'Find out the year of establishment for "{food_hall}".'+' return the response as raw json: {"year_established": 1980} or {"data": null} if the exact year is not available.'

    google_link = make_google_search(
        f'{food_hall} year established', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_renovation_history(food_hall: str, browser):
    """Returns the renovation history of the food hall."""
    instruction = "In your capacity as a market researcher, you are to uncover the renovation history of a food hall."
    prompt = f'Detail the renovation history of "{food_hall}".'+' return the response as raw json: {"renovation_history": "Details"} or {"data": null} if comprehensive details are not available.'

    google_link = make_google_search(
        f'{food_hall} renovation history', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_owner(food_hall: str, browser):
    """Returns the owner of the food hall."""
    instruction = "Your task as a market researcher is to identify the owner or owning entity of a food hall."
    prompt = f'Identify the owner of "{food_hall}". '+'return the response as raw json: {"owner": "Name", "contact": "ContactInfo"} or {"data": null} if the owner’s details are not directly available.'

    google_link = make_google_search(f'{food_hall} owner', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_management_company(food_hall: str, browser):
    """Returns the management company of the food hall."""
    instruction = "The aim of your market research is to find out which company manages a specific food hall."
    prompt = f'Find out the management company for "{food_hall}".'+' return the response as raw json: {"management_company": "CompanyName"} or {"data": null} if the details are not evident.'

    google_link = make_google_search(
        f'{food_hall} management company', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def updateDB(id: str, data: dict):
    """Updates the database with the data"""
    requests.post(f'http://localhost:3333/crawler/update/{id}', json=data)

def browser_research(browser, tasks, foodhall):
    """Executes a list of research tasks using the given browser instance."""
    for task in tasks:
        try:
            # Assuming each task function takes a 'food_hall' string and a 'browser' object
            # You might need to adjust this call depending on how your task functions are structured
            task_response = task(foodhall, browser)
            print(task.__name__ + f': {task_response}')
        except Exception as e:
            print(f"Error executing {task.__name__}: {e}")

def run_in_parallel(foodhall):
    # Initialize browser instances
    browser1 = webdriver.Chrome()
    browser2 = webdriver.Chrome()
    browser3 = webdriver.Chrome()
    browser4 = webdriver.Chrome()

    # Set window sizes for a 1920x1080 resolution, adjust these values based on your actual screen resolution
    root = tkinter.Tk()
    width = root.winfo_screenwidth()//2
    height = root.winfo_screenheight()//2
    # width = 1920 // 2
    # height = 1080 // 2

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
    all_tasks = [get_location, get_square_footage,get_number_of_food_stalls,get_types_of_food_stalls,get_demographic,get_local_area_composition,get_public_transport,get_parking_availability,get_foot_traffic_estimates,get_annual_visitor_count,get_lease_rates,get_occupancy_rate,get_year_established,get_renovation_history,get_owner,get_management_company]
    n = len(all_tasks)

    tasks1 = all_tasks[:4]
    tasks2 = all_tasks[4:8]
    tasks3 = all_tasks[8:12]
    tasks4 = all_tasks[12:]

    # Create and start threads for each set of tasks
    thread1 = threading.Thread(target=browser_research, args=(browser1, tasks1,foodhall))
    thread2 = threading.Thread(target=browser_research, args=(browser2, tasks2,foodhall))
    thread3 = threading.Thread(target=browser_research, args=(browser3, tasks3,foodhall))
    thread4 = threading.Thread(target=browser_research, args=(browser4, tasks4,foodhall))

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

    pass


if __name__ == '__main__':
    run_in_parallel('alton food hall')
