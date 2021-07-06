from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

class Google_Sheet_Inputer:
    def __init__(self):
        """Uses selenium to enter given zillow data into google sheet"""
        # Initializes selenium
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def input_list(self, zillow_data, google_sheet_link):
        """Enters the given zillow data into the given google sheet"""
        # Loops through the list of properties
        for property_to_enter in zillow_data:
            # Enters the google sheet link into the browser
            self.driver.get(google_sheet_link)
            # Find the elements for the price, address and link
            price_field = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_field = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Enters the price, address and link into the elements
            price_field.send_keys(property_to_enter['price'])
            address_field.send_keys(property_to_enter['address'])
            link_field.send_keys(property_to_enter['link'])
            # Find and click the submit button
            enter_button = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
            enter_button.click()
        # Exit out of the browser
        self.driver.quit()
