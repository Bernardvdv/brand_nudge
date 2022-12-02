from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests
import lxml
import time
import helpers
import constants


# Generate fake Request headers
ua = UserAgent()
headers = {"user-agent": ua.chrome}

# Establish DB connection
db_conn = helpers.create_connection_mysql()
mycursor = db_conn.cursor()


r = requests.get(constants.URL, headers=headers, timeout=20, allow_redirects=True,)
soup = bs(r.text, "lxml")

products = helpers.prepare_data(soup)

for product in products:
    url = product["url"]
    r = requests.get(url, headers=headers, timeout=20, allow_redirects=True,)
    soup = bs(r.text, "lxml")

    p_grid = soup.find("div", {"id": "layout"})
    p_name = p_grid.find("h1", {"data-testid": "product:title"}).text
    p_prize = p_grid.find("span", {"data-testid": "product:price"}).text
    p_rating = p_grid.find("div", {"data-testid": "product:starRatings"}).get("title")
    p_guarentees = p_grid.find(
        "p", {"data-testid": "product:included-guarantees:title"}
    ).text
    p_delivery = p_grid.find("div", {"data-testid": "product:delivery-message"}).text
    # Push row data to DB
    helpers.import_to_db(p_name, p_prize, p_rating, p_guarentees, p_delivery, url)
    # Attempt to prevent rate limiting
    time.sleep(5)
