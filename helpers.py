import constants
import mysql.connector
from datetime import datetime
import json


def create_connection_mysql():
    try:
        conn = mysql.connector.connect(
            host=constants.DBHOST,
            user=constants.USERNAME,
            passwd=constants.PASSWORD,
            database=constants.DATABASE,
        )
        return conn
    except Exception as e:
        print(e)
        pass


def import_to_db(name, price, rating, guerentee, delivery, url):
    try:
        db_conn = create_connection_mysql()
        mycursor = db_conn.cursor()
        sql = """INSERT INTO products (ProductsName, ProductsPrice, ProductsRating, ProductsGuarentee, ProductsDelivery, ProductsUrl, DateTimeInserted)
         VALUES (%s, %s, %s, %s, %s, %s, %s);"""

        params = (name, price, rating, guerentee, delivery, url, datetime.now())

        mycursor.execute(sql, params)
        db_conn.commit()

        return
    except Exception as e:
        print("SQL Error")
        print(e)
        pass


def prepare_data(soup):
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
