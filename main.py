import zillow_data
import google_sheet_inputer

# Google Form for the data to be entered in
GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSfInRPaTIstSSZMZ-YBwDdqzbmqCs1zIVGnxmLjMF_7qSiPtQ/viewform?usp=sf_link'
# Zillow Link with the required criteria
ZILLOW_PROPERTY_LINK = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.60885275793457%2C%22east%22%3A-122.29883231115723%2C%22south%22%3A37.65728766875633%2C%22north%22%3A37.978402512224335%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A916433%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

# Zillow_Data scrapes the price,list and address from Zillow.com. Google_Sheet_Inputer enters the price, list and address into the given google sheet.
Zillow_Data = zillow_data.Zillow_Data()
Google_Sheet_Inputer = google_sheet_inputer.Google_Sheet_Inputer()
Google_Sheet_Inputer.input_list(zillow_data=Zillow_Data.give_zillow_data(ZILLOW_PROPERTY_LINK),
                                google_sheet_link=GOOGLE_FORM_LINK)
