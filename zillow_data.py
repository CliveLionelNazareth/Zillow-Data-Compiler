from bs4 import BeautifulSoup
import requests
import re


class Zillow_Data():
    def __init__(self):
        """Uses BeautifulSoup to return the price, list and address of properties from zillow link"""
        # Zillow requires Headers to load webpage through BeautifulSoup
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

    def give_zillow_data(self, zillow_url):
        """Returns a list of dictionaries containing the price, address and link"""
        # Request the webpage and feed it through an html parser
        response = requests.get(zillow_url, headers=self.headers)
        response.raise_for_status()
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        # Generate the list of price, address and link elements
        price_list = soup.select("div.list-card-heading div.list-card-price")
        address_list = soup.select("div.list-card-info address.list-card-addr")
        link_list = soup.select("div.list-card-info a.list-card-link")
        zillow_data = []
        # Put the elements into a list of dictionaries
        for current_house in range(len(price_list)):
            zillow_data.append({
                # Remove all non numeric characters
                'price': re.sub(r"\D+", "", price_list[current_house].getText())[0:4],
                'address': address_list[current_house].getText(),
                # Add www.zillow.com in case the link doesn't come with it
                'link': (link_list[current_house]['href'] if 'zillow' in link_list[current_house][
                    'href'] else "https://www.zillow.com" + link_list[current_house]['href'])
            })
        return zillow_data
