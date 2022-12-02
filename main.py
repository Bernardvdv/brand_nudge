from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests
import lxml
import json
import time
import sys
import mysql.connector
from datetime import datetime

DBHOST = "localhost"
USERNAME = "test_user"
PASSWORD = "Th1515n0t@53cur3p@55w0rd!"
DATABASE = "brandnudge"


def create_connection_mysql():

    try:
        conn = mysql.connector.connect(
            host=DBHOST, user=USERNAME, passwd=PASSWORD, database=DATABASE,
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

        return 1
    except Exception as e:
        print("SQL Error")
        print(e)
        pass


db_conn = create_connection_mysql()
mycursor = db_conn.cursor()


ua = UserAgent()
headers = {"user-agent": ua.chrome}


url = "https://www.johnlewis.com/browse/electricals/coffee-machines/view-all-coffee-machines/_/N-afu"

# r = requests.get(url, headers=headers, timeout=20, allow_redirects=True,)
# soup = bs(r.text, "lxml")

# products = soup.find("div", {"data-test-id": "product-grid"})
# # print(products)
# raw = products.find_all("script")
# test = str(raw)
# test = test.replace('<script type="application/ld+json">', "").replace("</script>", "")
# y = json.loads(test)
t = 1
y = {
    "@type": "ItemList",
    "@context": "https://schema.org",
    "numberOfItems": "(77)",
    "itemListElement": [
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-krups-pixie-xn304t40-coffee-machine-titanium/p4247645",
            "position": 1,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-citiz-milk-coffee-machine-by-magimix/p2845232",
            "position": 2,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-lattissima-touch-en560-coffee-machine-by-delonghi/p5301599",
            "position": 3,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/tassimo-by-bosch-suny-special-edition-tas3102gb-coffee-machine-black/p6250001",
            "position": 4,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-plus-xn903840-coffee-machine-by-krups-with-pods/p4801147",
            "position": 5,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-magnifica-ecam290-22-b-evo-fully-automatic-bean-to-cup-coffee-machine-black/p5795985",
            "position": 6,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-citiz-coffee-machine-by-magimix-chrome-effect/p2907176",
            "position": 7,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-ec260-bk-stilosa-espresso-coffee-machine-black/p5131112",
            "position": 8,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-barista-express-bean-to-cup-coffee-machine/p3501284",
            "position": 9,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-barista-touch-coffee-machine-black-truffle/p6263795",
            "position": 10,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-next-11709-coffee-machine-by-magimix-chrome/p5233555",
            "position": 11,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-a-modo-mio-jolie-espresso-coffee-machine-white/p4851241",
            "position": 12,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-ec785-dedica-metallic-traditional-coffee-machine/p5570739",
            "position": 13,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-barista-express-impress-coffee-machine-black-truffle/p6263799",
            "position": 14,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-citiz-milk-coffee-machine-by-magimix-chrome-effect/p2905508",
            "position": 15,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-ses878-the-barista-pro-coffee-machine/p4081414",
            "position": 16,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-pop-coffee-pod-machine-by-krups/p109126018",
            "position": 17,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-en650-gran-lattissima-capsule-coffee-machine-by-delonghi/p4403083",
            "position": 18,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/bosch-styline-tka8013gb-filter-coffee-maker/p5649698",
            "position": 19,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/john-lewis-pump-espresso-coffee-machine-stainless-steel/p4839988",
            "position": 20,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-duo-temp-pro-espresso-coffee-machine/p1749201",
            "position": 21,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-capsule-coffee-machine-by-smeg/p5176027",
            "position": 22,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-tq703gb7-eq700-bean-to-cup-coffee-machine-with-home-connect/p5577624",
            "position": 23,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-barista-express-impress-coffee-machine-stainless-steel/p6354148",
            "position": 24,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/smeg-ecf01-coffee-machine/p3081576",
            "position": 25,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/john-lewis-pump-espresso-coffee-machine-with-milk-frother-stainless-steel/p4839837",
            "position": 26,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-ses500bss-bambino-plus-coffee-machine-silver/p3779133",
            "position": 27,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-ti9573x9gb-eq9s700-bean-to-cup-coffee-machine-with-dual-hopper-and-home-connect/p5577622",
            "position": 28,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-a-modo-mio-jolie-plus-coffee-machine-with-milk-frother/p3443339",
            "position": 29,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-plus-deluxe-coffee-machine-aeroccino-set-black/p6250024",
            "position": 30,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-barista-touch-barista-quality-bean-to-cup-coffee-machine/p3349117",
            "position": 31,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-tq503gb1-eq-500-bean-to-cup-coffee-machine-black/p5075132",
            "position": 32,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-dinamica-ecam370-95-t-plus-fully-automatic-bean-to-cup-coffee-machine-titanium/p4189584",
            "position": 33,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-creatista-plus-coffee-machine-by-sage-black-truffle/p3116015",
            "position": 34,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-ec9355-la-specialista-prestigio-bean-to-cup-espresso-coffee-machine/p5570741",
            "position": 35,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-plus-le-coffee-machine-by-magimix/p4323194",
            "position": 36,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-primadonna-ecam610-75-mb-soul-fully-automatic-bean-to-cup-coffee-machine-metal-black/p5129276",
            "position": 37,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-maestosa-epam960-75-glm-fully-automatic-bean-to-cup-coffee-machine-metal-black/p4187134",
            "position": 38,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/smeg-bcc02-bean-to-cup-coffee-machine/p5599733",
            "position": 39,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-oracle-touch-fully-automatic-bean-to-cup-coffee-machine-black-truffle/p4797480",
            "position": 40,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-sage-sne500bks-creatista-uno-coffee-machine-black/p3751335",
            "position": 41,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-voicy-coffee-machine/p5567626",
            "position": 42,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-pop-coffee-pod-machine-by-magimix/p109265036",
            "position": 43,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-ec9665-m-la-specialista-maestro-bean-to-cup-espresso-coffee-machine/p5129277",
            "position": 44,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-a-modo-mio-desea-coffee-machine/p4019308",
            "position": 45,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-oracle-bean-to-cup-coffee-machine/p3303705",
            "position": 46,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-ti9553x1gb-eq-9-plus-bean-to-cup-coffee-machine-black/p4245180",
            "position": 47,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-oracle-touch-fully-automatic-bean-to-cup-coffee-machine/p3336790",
            "position": 48,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-atelier-coffee-machine-by-krups/p5066416",
            "position": 49,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-primadonna-elite-experience-ecam650-85-ms-fully-automatic-bean-to-cup-coffee-machine-metal-silver/p3244255",
            "position": 50,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/jura-e8-coffee-machine/p5321567",
            "position": 51,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-magnifica-ecam290-81-tb-evo-fully-automatic-bean-to-cup-coffee-machine-titanium/p5771986",
            "position": 52,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/lavazza-jolie-coffee-machine-black/p4509055",
            "position": 53,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/jura-e6-15511-coffee-machine-black/p6271650",
            "position": 54,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-oracle-bes980uk-coffee-machine-black-truffle/p5217656",
            "position": 55,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-ti351209gb-eq-300-bean-to-cup-coffee-machine-black/p5075143",
            "position": 56,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/jura-ena-4-bean-to-cup-coffee-machine/p5636410",
            "position": 57,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-bambino-stainless-steel-coffee-machine/p6263794",
            "position": 58,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-dedica-arte-metallics-espresso-coffee-machine/p6262524",
            "position": 59,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/jura-ena-8-signature-line-coffee-machine-silver/p109527258",
            "position": 60,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-plus-coffee-machine-by-magimix/p3343799",
            "position": 61,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-citiz-coffee-machine-black/p5521908",
            "position": 62,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/tassimo-by-bosch-joy-tas4502ngb-coffee-machine/p6250004",
            "position": 63,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/siemens-tp705gb1-eq700-home-connect-bean-to-cup-fully-automatic-freestanding-coffee-machine-graphite/p6250005",
            "position": 64,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-sage-creatista-plus-coffee-machine-smoked-hickory/p5067118",
            "position": 65,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-creatista-plus-coffee-machine-by-sage-stainless-steel/p5067057",
            "position": 66,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-dinnamica-plus-fully-auto-coffee-machine-black/p6262527",
            "position": 67,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/smeg-dcf02-drip-filter-coffee-machine/p5176025",
            "position": 68,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/sage-the-precision-brewer-coffee-machine/p3811244",
            "position": 69,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/jura-z10-bean-to-cup-coffee-machine/p5636413",
            "position": 70,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-creatista-pro-sne900bss-coffee-machine-by-sage-stainless-steel/p4879259",
            "position": 71,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/delonghi-ec9155-mb-la-specialista-arte-bean-to-cup-espresso-coffee-machine/p5771975",
            "position": 72,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-next-coffee-machine-by-krups/p5027090",
            "position": 73,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-vertuo-next-coffee-maker-by-magimix/p5019464",
            "position": 74,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/fisher-paykel-eb60dsxb2-60cm-built-in-bean-to-cup-coffee-machine-gloss-black/p4061365",
            "position": 75,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/nespresso-essenza-mini-coffee-machine-by-krups/p3188228",
            "position": 76,
        },
        {
            "@type": "ListItem",
            "url": "https://www.johnlewis.com/neff-c17ks61n0-built-in-bean-to-cup-coffee-machine-stainless-steel/p1931539",
            "position": 77,
        },
    ],
}

for product in y["itemListElement"]:
    time.sleep(5)
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
    import_to_db(p_name, p_prize, p_rating, p_guarentees, p_delivery, url)

