import requests
from BeautifulSoup import BeautifulSoup
import re


def trade_spider(max_pages):
    prices = []
    mileage = []
    page = 1
    while page <= max_pages:
    #url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        url = "https://www.truecar.com/used-cars-for-sale/listings/toyota/camry/?page=" + str(page) + "&used_opt=usedmake%3Atoyota"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for car_price in soup.findAll('p', {'class': 'price'}):
            price = re.sub(r'\W+', '', car_price.string)
            prices.append(price)
    
    
        for miles in soup.findAll('ul', {'class': 'vehicle-info list-unstyled'}):

            cleaned_miles = re.sub('[^0-9]','', str(miles.li))
            mileage.append(cleaned_miles)
        page += 1
    mileage = map(int, mileage)
    prices = map(int, prices)
    print "mean mileage" + str(sum(mileage)/len(mileage)) 
    print "mean price of toyota camry" + str(sum(prices)/len(prices))
    print mileage
    print prices
    
    
    
   
    

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)

trade_spider(3)