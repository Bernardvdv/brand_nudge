"""John Lewis product main scraper file."""

from bs4 import BeautifulSoup
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


def main():
    """Initiate scraper and validate data."""
    counter = 0
    r = requests.get(
        constants.URL,
        headers=headers,
        timeout=20,
        allow_redirects=True
    )
    soup = BeautifulSoup(r.text, "lxml")

    # Get schema data and convert to nested list
    products = helpers.prepare_data(soup)
    # Create list of URL's from prepared data
    url_list = helpers.get_urls(products)
    url_count = len(url_list)

    for url in url_list:
        r = requests.get(
            url,
            headers=headers,
            timeout=20,
            allow_redirects=True
        )
        soup = BeautifulSoup(r.text, "lxml")

        row_data = helpers.get_row_data(soup)
        # Push row data to DB
        helpers.import_to_db(
            row_data[0],
            row_data[1],
            row_data[2],
            row_data[3],
            row_data[4],
            url
        )
        # Attempt to prevent rate limiting
        counter += 1
        time.sleep(1)
    # Confirm if all URL's were scraped
    helpers.validate_data(url_count, counter)


if __name__ == "__main__":
    main()
