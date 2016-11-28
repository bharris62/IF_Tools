import os
from insulinfirst.extensions import db
from insulinfirst.models import Product
from amazon.api import AmazonAPI
import re


def amazon_strips():
    amazon = AmazonAPI('AKIAJLW4JVOUA6L62PKQ', 'z0+px3hgEbAR5zqTjSJL70k+JyiS87ps4qEbgA7g', 'insulinfirst-20')

    prod = amazon.search(Keywords='diabetes blood test strips', SearchIndex='All')
    rows_logged = 0
    for i in prod:
        product = Product()
        # product manufacturer
        prod_manufacturerer = i.publisher
        product.product_manufacturer = prod_manufacturerer

        # description of product / Product Name
        prod_name = i.title
        product.product_name = prod_name

        # Price of Product
        prod_price = i.price_and_currency[0]
        product.product_price = prod_price

        # Image of product
        image = i.medium_image_url
        product.product_image = image

        # offer url
        url = i.offer_url
        product.product_url = url

        website = 'Amazon'
        product.product_dealer = website

        prod_type = 'Test Strips'
        product.product_type = prod_type

        prod_description = ''
        product.product_description = prod_description

        try:
            quantity = re.findall(r"[-+]?\d*\.\d+|\d+", prod_name)[-1]

            pps = format(float(prod_price) / float(quantity), '.2f')
            if float(pps) > 2:
                pps = 1000
            product.product_price_per_strip = pps

        except IndexError:
            pass


        rows_logged += 1
        db.session.add(product)
        db.session.commit()

    print("logged {} rows".format(rows_logged))