from flask import Flask, request, Response
from webcrawler import CrawlerTools
from selenium import webdriver
from models import FoodHall

import os
from dotenv import load_dotenv
from convex import ConvexClient

load_dotenv(".env.local")
load_dotenv()

client = ConvexClient(os.getenv("CONVEX_URL"))


app = Flask(__name__)


@app.post("/db/add")
def add_food_hall():
    if not request.json:
        return Response("No data provided", status=400)

    client.mutation("findings:createFoodHall", request.json)
    return "done"


@app.route("/")
def hello_world():
    res = {
        "message": "why hello there!",
        "other_stuff": "you should give us da dub!"
    }
    return res


@app.get("/crawler/<search_key>")
def google_search(search_key):
    driver = webdriver.Chrome()
    links = CrawlerTools.make_google_search(search_key, driver)
    return links


@app.get("/crawler/research/<food_hall_name>")
def research(food_hall_name):
    driver = webdriver.Chrome()

    links = CrawlerTools.make_google_search(food_hall_name, driver)
    return links


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3333)
