from flask import Flask, request, Response
from webcrawler import ResearchHall
from selenium import webdriver

import os
from dotenv import load_dotenv
from convex import ConvexClient

load_dotenv(".env.local")
load_dotenv()

client = ConvexClient(os.getenv("CONVEX_URL"))

app = Flask(__name__)


@app.get("/crawler/new/<search_key>")
def start_new_crawl(search_key):
    id = client.mutation("findings:createFoodHall", {"name": search_key})
    ResearchHall.main(id, search_key, client)
    return "Done. Success."


@app.route("/done")
def finish_page():
    # html
    return """
    <body style="width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; font-size: 50px; font-family: monospace">Done</body>
    
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3333)
