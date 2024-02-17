from CrawlerTools import make_google_search
from selenium import webdriver
from openai import OpenAI
import json

client = OpenAI(api_key='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')

def get_location(food_hall:str, browser):
    """returns location of food hall"""
    pass

def get_square_footage(food_hall:str, browser):
    """returns get_square_footage of food hall"""
    pass

def get_number_of_food_stalls(food_hall:str, browser):
    """returns number of food, bar, and retail stalls of food hall"""
    pass

def get_types_of_food_stalls(food_hall:str, browser):
    """returns types of food stalls in food hall"""
    pass

def get_demographic(food_hall: str, browser):
    """
    Returns demographic information of the area surrounding the food hall.
    Example data: Population density, median income, age distribution.
    Source: Google Maps API, Census Bureau websites.
    """
    pass

def get_local_area_composition(food_hall: str, browser):
    """
    Returns information on the local area composition around the food hall.
    Example data: Mix of residential/commercial areas, presence of parks/schools.
    Source: Google Maps for businesses and amenities nearby.
    """
    pass

def get_public_transport(food_hall: str, browser):
    """
    Returns public transport options available near the food hall.
    Example data: Nearby bus stops, train stations, and their service routes.
    Source: Google Maps API, local public transport authority websites.
    """
    pass

def get_parking_availability(food_hall: str, browser):
    """
    Returns parking availability information for the food hall.
    Example data: Number of parking spots, parking fees, peak time availability.
    Source: Google Maps, local government websites.
    """
    pass

def get_foot_traffic_estimates(food_hall: str, browser):
    """
    Returns foot traffic estimates near the food hall.
    Example data: Average daily or hourly foot traffic, peak times.
    Source: Place.ai, similar web-based traffic analytics services.
    """
    pass

def get_annual_visitor_count(food_hall: str, browser):
    """
    Returns the annual visitor count of the food hall.
    Example data: Total number of visitors in a year, comparison with previous years.
    Source: Place.ai, local business reports.
    """
    pass

def get_lease_rates(food_hall: str, browser):
    """
    Returns lease rates for the food hall.
    Example data: Average lease rate per square foot, comparison with market rates.
    Source: LoopNet, commercial real estate listing services.
    """
    pass

def get_occupancy_rate(food_hall: str, browser):
    """
    Returns the occupancy rate of the food hall.
    Example data: Percentage of occupied space, comparison with industry average.
    Source: LoopNet, real estate market reports.
    """
    pass

def get_year_established(food_hall: str, browser):
    """
    Returns the year the food hall was established.
    Example data: Year of establishment, historical significance.
    Source: Google search, historical data, food hall's official website.
    """
    pass

def get_renovation_history(food_hall: str, browser):
    """
    Returns the renovation history of the food hall.
    Example data: Dates and types of past renovations, permits issued.
    Source: Building permits from local government databases.
    """
    pass

def get_owner(food_hall: str, browser):
    """
    Returns the owner of the food hall.
    Example data: Name of the owner or owning entity, contact information.
    Source: Property tax records, local assessor's office websites.
    """
    pass

def get_management_company(food_hall: str, browser):
    """
    Returns the management company of the food hall.
    Example data: Name of the management company, services provided.
    Source: The food hall's official website, local business registries.
    """
    pass



if __name__ == '__main__':
    browser = webdriver.Chrome()
    print(make_google_search("hamster"))