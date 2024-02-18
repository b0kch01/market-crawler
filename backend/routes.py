from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from webcrawler import ResearchHall
from selenium import webdriver
import threading

import os
from dotenv import load_dotenv
from convex import ConvexClient

load_dotenv(".env.local")
load_dotenv()

client = ConvexClient(os.getenv("NEXT_PUBLIC_CONVEX_URL"))

app = Flask(__name__)


@app.get("/crawler/new/<search_key>")
@cross_origin()
def start_new_crawl(search_key):

    def task(client, search_key: str):
        id = client.mutation("findings:createFoodHall", {"name": search_key})
        ResearchHall.run_in_parallel(search_key, id, client=client)

    threading.Thread(target=task, args=(client, search_key)).start()

    return "{ 'status': 'success' }"


@app.route("/done")
def finish_page():
    # html
    return """
    <body style="width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; font-size: 50px; font-family: monospace">Done</body>
    
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3333)
