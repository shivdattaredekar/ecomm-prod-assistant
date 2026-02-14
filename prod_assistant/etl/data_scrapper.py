import os
import re
from bs4 import BeautifulSoup
import undetected_chromedriver as uc #type:ignore
from selenium.webdriver.common.by import By #type:ignore
from selenium.webdriver.common.keys import Keys #type:ignore
from selenium.webdriver.common.action_chains import ActionChains #type:ignore

class FlipkartScrapper:

    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def get_top_reviews(self, product_url, count=2):
        pass

    def scrape_flipkart_products(self, query, max_produccts=1, review_count=2):
        """_summary_

        Args:
            query (_type_): _description_
            max_produccts (int, optional): _description_. Defaults to 1.
            review_count (int, optional): _description_. Defaults to 2.
        """
        pass

    def save_to_csv(self, data, filename="product_reviews.csv"):
        """_summary_

        Args:
            data (_type_): _description_
            filename (str, optional): _description_. Defaults to "product_reviews.csv".
        """
        pass

