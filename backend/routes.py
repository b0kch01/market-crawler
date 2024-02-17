from flask import Flask
from webcrawler import CrawlerTools
from selenium import webdriver
from models import FoodHall

# flask --app main run

app = Flask(__name__)

@app.route("/")
def hello_world():
    res = {
        "message": "why hello there!",
        "other_stuff": "you should give us da dub!"
    }
    return res

@app.route("/crawler/<search_key>")
def google_search(search_key):
    driver = webdriver.Chrome()
    links = CrawlerTools.make_google_search(search_key, driver)
    return links

@app.route("/crawler/research/<food_hall_name>")
def google_search(food_hall_name):
    driver = webdriver.Chrome()

    links = CrawlerTools.make_google_search(food_hall_name, driver)
    return links