from webcrawler.CrawlerTools import make_google_search
from webcrawler.CrawlerTools import scrape_page_text
from selenium import webdriver
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

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
    prompt = f'Given this text content, help me figure out the location of this food hall ({food_hall}), make sure answer is in form like "city, state" like Irvine, CA: '

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
    prompt = f'Given this text content, help me figure out the square footage of this food hall ({food_hall}), make sure answer is in form like "10000" (int, JUST THE NUMBER). If you cannot find data, then return "None": '

    google_link = make_google_search(
        f'{food_hall} square footage', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(location_instruction, prompt + webcontent)
    return res


def get_number_of_food_stalls(food_hall: str, browser):
    """returns number of food, bar, and retail stalls of food hall"""
    location_instruction = "You are a market researcher and you are helping me find information about certain food halls."
    prompt = f'Given this text content, help me figure out the number of food stalls, bar stalls, and retail stalls in this food hall ({food_hall}), make sure answer is in form like "food:3,bars:4,retail:3" (str:int,str:int,str:int) JUST THIS. If you cannot find data, then return "None": '

    google_link = make_google_search(
        f'{food_hall} number of food stalls', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(location_instruction, prompt + webcontent)
    return res

# GPT Generated all below... this is what we want to do with the universal scraper...


def get_types_of_food_stalls(food_hall: str, browser):
    """Returns types of food stalls in food hall"""
    instruction = "You are a market researcher and you are helping me find information about the types of food stalls in certain food halls."
    prompt = f'Given this text content, help me list the types of food stalls available in this food hall ({food_hall}). Provide the types in a list format, e.g., ["Mexican", "Italian", "Japanese"]. If you cannot find data, then return "None": '

    google_link = make_google_search(
        f'{food_hall} types of food stalls', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_demographic(food_hall: str, browser):
    """Returns demographic information of the area surrounding the food hall."""
    instruction = "You are a market researcher and you are tasked with gathering demographic information about the area surrounding a specific food hall."
    prompt = f'Analyze the text content to provide demographic information (population density, median income, age distribution) of the area surrounding the food hall ({food_hall}). If you cannot find specific data, provide a general overview based on available information: '

    google_link = make_google_search(
        f'{food_hall} area demographics', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_local_area_composition(food_hall: str, browser):
    """Returns information on the local area composition around the food hall."""
    instruction = "You are a market researcher and your objective is to understand the composition of the area surrounding a food hall."
    prompt = f'Evaluate the text content to describe the mix of residential and commercial areas, and the presence of parks, schools, or other notable amenities near the food hall ({food_hall}). Summarize the findings succinctly: '

    google_link = make_google_search(
        f'{food_hall} surrounding area composition', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_public_transport(food_hall: str, browser):
    """Returns public transport options available near the food hall."""
    instruction = "You are a market researcher, aiming to find out about public transport options available near a food hall."
    prompt = f'Gather and summarize information about the nearby bus stops, train stations, and their service routes for the food hall ({food_hall}). If data is scarce, provide an overview of the public transport accessibility based on available information: '

    google_link = make_google_search(
        f'{food_hall} public transport options', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_parking_availability(food_hall: str, browser):
    """Returns parking availability information for the food hall."""
    instruction = "You are a market researcher focusing on parking availability for a particular food hall."
    prompt = f'Analyze the text to provide details on the number of parking spots, parking fees, and peak time availability for the food hall ({food_hall}). If such data is not available, suggest based on the context: '

    google_link = make_google_search(
        f'{food_hall} parking availability', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_foot_traffic_estimates(food_hall: str, browser):
    """Returns foot traffic estimates near the food hall."""
    instruction = "As a market researcher, your task is to estimate the foot traffic around a specific food hall."
    prompt = f'Deduce from the content the average daily or hourly foot traffic, including peak times, near the food hall ({food_hall}). If direct estimates are unavailable, provide an educated guess based on available information: '

    google_link = make_google_search(
        f'{food_hall} foot traffic estimates', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_annual_visitor_count(food_hall: str, browser):
    """Returns the annual visitor count of the food hall."""
    instruction = "You are tasked with finding the annual visitor count for a food hall as part of a market research project."
    prompt = f'Extract and summarize information on the total number of visitors in a year and, if available, a comparison with previous years for the food hall ({food_hall}). If no specific numbers are found, provide an overview based on the context: '

    google_link = make_google_search(
        f'{food_hall} annual visitor count', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_lease_rates(food_hall: str, browser):
    """Returns lease rates for the food hall."""
    instruction = "Your objective as a market researcher is to determine the lease rates for spaces within a specific food hall."
    prompt = f'Please provide the average lease rate per square foot and, if possible, a comparison with market rates for the food hall ({food_hall}). If precise rates are not available, give a general assessment based on the gathered information: '

    google_link = make_google_search(f'{food_hall} lease rates', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_occupancy_rate(food_hall: str, browser):
    """Returns the occupancy rate of the food hall."""
    instruction = "As a market researcher, it's your job to find out the occupancy rate of a given food hall."
    prompt = f'Analyze the text to provide the percentage of occupied space and compare it with the industry average for the food hall ({food_hall}). If such data is not directly available, make an inference based on available information: '

    google_link = make_google_search(
        f'{food_hall} occupancy rate', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_year_established(food_hall: str, browser):
    """Returns the year the food hall was established."""
    instruction = "Your role as a market researcher involves finding out when a food hall was first established."
    prompt = f'Gather information on the year of establishment and any historical significance for the food hall ({food_hall}). If the exact year is not available, provide a historical overview: '

    google_link = make_google_search(
        f'{food_hall} year established', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_renovation_history(food_hall: str, browser):
    """Returns the renovation history of the food hall."""
    instruction = "In your capacity as a market researcher, you are to uncover the renovation history of a food hall."
    prompt = f'Please detail the dates and types of past renovations, including any permits issued for the food hall ({food_hall}). If comprehensive details are not available, provide a summary based on accessible data: '

    google_link = make_google_search(
        f'{food_hall} renovation history', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_owner(food_hall: str, browser):
    """Returns the owner of the food hall."""
    instruction = "Your task as a market researcher is to identify the owner or owning entity of a food hall."
    prompt = f'Discover and report the name of the owner or owning entity, including contact information for the food hall ({food_hall}). If the owner\'s details are not directly available, suggest likely ownership based on the context: '

    google_link = make_google_search(f'{food_hall} owner', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def get_management_company(food_hall: str, browser):
    """Returns the management company of the food hall."""
    instruction = "The aim of your market research is to find out which company manages a specific food hall."
    prompt = f'Please provide information on the name of the management company and the services it offers for the food hall ({food_hall}). If the management company\'s details are not evident, give an overview based on available data: '

    google_link = make_google_search(
        f'{food_hall} management company', browser, 1)[0]
    webcontent = scrape_page_text(google_link, browser)

    res = gpt_request(instruction, prompt + webcontent)
    return res


def updateDB(id: str, data: dict):
    """Updates the database with the data"""
    requests.post(f'http://localhost:3333/crawler/update/{id}', json=data)


def main(id: str, name: str, client):
    # Placeholder for browser initialization (e.g., Selenium WebDriver)
    # Replace None with actual browser initializer like webdriver.Chrome()
    browser = webdriver.Safari()

    food_hall_name = name

    # Assuming each function returns a string or JSON for simplicity in printing
    print("Research Results:")
    location = get_location(food_hall_name, browser)
    client.mutation("findings:updateFoodHall", {
                    "id": id, "location": location})

    # print("Square Footage:", get_square_footage(food_hall_name, browser))
    # print("Number of Food Stalls:",
    #       get_number_of_food_stalls(food_hall_name, browser))
    # print("Types of Food Stalls:",
    #       get_types_of_food_stalls(food_hall_name, browser))
    # print("Demographic Information:", get_demographic(food_hall_name, browser))
    # print("Local Area Composition:",
    #       get_local_area_composition(food_hall_name, browser))
    # print("Public Transport Options:",
    #       get_public_transport(food_hall_name, browser))
    # print("Parking Availability:",
    #       get_parking_availability(food_hall_name, browser))
    # print("Foot Traffic Estimates:",
    #       get_foot_traffic_estimates(food_hall_name, browser))
    # print("Annual Visitor Count:",
    #       get_annual_visitor_count(food_hall_name, browser))
    # print("Lease Rates:", get_lease_rates(food_hall_name, browser))
    # print("Occupancy Rate:", get_occupancy_rate(food_hall_name, browser))
    # print("Year Established:", get_year_established(food_hall_name, browser))
    # print("Renovation History:", get_renovation_history(food_hall_name, browser))
    # print("Owner:", get_owner(food_hall_name, browser))

    company = get_management_company(food_hall_name, browser)
    client.mutation("findings:updateFoodHall", {
                    "id": id, "managementCompany": company})


if __name__ == '__main__':
    main()
