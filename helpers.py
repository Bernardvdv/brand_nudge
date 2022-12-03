"""John Lewis scraper helper methods."""

import constants
import mysql.connector
from datetime import datetime
import json


def create_connection_mysql():
    """Initiate connection to MySQL."""
    conn = mysql.connector.connect(
        host=constants.DBHOST,
        user=constants.USERNAME,
        passwd=constants.PASSWORD,
        database=constants.DATABASE
    )
    return conn


def import_to_db(name, price, rating, guerentee, delivery, url):
    """Store each row of processed data."""
    try:
        date = datetime.now()
        db_conn = create_connection_mysql()
        mycursor = db_conn.cursor()
        sql = """INSERT INTO products (
            ProductsName,
            ProductsPrice,
            ProductsRating,
            ProductsGuarentee,
            ProductsDelivery,
            ProductsUrl,
            DateTimeInserted
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);"""

        params = (name, price, rating, guerentee, delivery, url, date)

        mycursor.execute(sql, params)
        db_conn.commit()

        return
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        pass


def prepare_data(soup):
    """Prepare soup object to allow easy processing."""
    product_grid = soup.find("div", {"data-test-id": "product-grid"})

    # Get the schema
    schema_products = product_grid.find_all("script")
    # Convert schema to string for sanitization
    schema_products_str = str(schema_products)

    cleaned_schema_products = schema_products_str.replace(
        '<script type="application/ld+json">', ""
    ).replace("</script>", "")

    # Convert data back to nested list
    product_list = json.loads(cleaned_schema_products)

    products = product_list[0]["itemListElement"]
    return products


def get_urls(products):
    """Create a list of URL's from the prepared data."""
    url_list = list()
    for x in products:
        url_list.append(x["url"])
    return url_list


def get_row_data(soup):
    """Process cleaned data and extract required info."""
    p_grid = soup.find("div", {"id": "layout"})
    try:
        p_name = p_grid.find("h1", {"data-testid": "product:title"}).text
    except:
        p_name = None
    try:
        p_prize = p_grid.find("span", {"data-testid": "product:price"}).text
    except:
        p_prize = None
    try:
        p_rating = p_grid.find("div", {"data-testid": "product:starRatings"}) \
            .get("title")
    except:
        p_rating = None
    try:
        p_guarentees = p_grid.find(
            "p", {"data-testid": "product:included-guarantees:title"}
        ).text
    except:
        p_guarentees = None
    try:
        p_delivery = p_grid.find(
            "div", {"data-testid": "product:delivery-message"}
        ).text
    except:
        p_delivery = None

    return [p_name, p_prize, p_rating, p_guarentees, p_delivery]


def validate_data(url_count, counter):
    """Validate lenght of URl's and count of scraped URL's are a match."""
    if url_count != counter:
        raise Exception("Sorry, looks like not all URL's where collected")
    return
