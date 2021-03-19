#imports the two modules we will need. 
import requests
from bs4 import BeautifulSoup

#Add your own link in the quotation marks!
source = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=Iphone&_sacat=0&LH_TitleDesc=0&_sop=1&LH_Auction=1&rt=nc&Model=Apple%2520iPhone%25208%7CApple%2520iPhone%25207%7CApple%2520iPhone%25208%2520Plus&_dcat=9355').text
soup = BeautifulSoup(source, 'lxml')
items = soup.find('li', class_='s-item')


#Goes to specifc parts of the HTML, scrapes out the item, and then prints it in the results. Loops through all the pages. 
for items in soup.find_all('li', class_='s-item'):
    try:
        item_title = items.find('h3', class_='s-item__title').text
    except Exception as e:
        item_title = 'None'
    print(item_title)
    try:
        item_desc = items.find('div', class_='s-item__subtitle').text
    except Exception as e:
        item_desc = 'None'
    print(item_desc)
    try:
        item_price = items.find('span', class_='s-item__price').text
    except Exception as e:
        item_price = 'None'
    print(item_price)
    try:
        item_shipping = items.find('span', class_='s-item__shipping s-item__logisticsCost').text
    except Exception as e:
        item_shipping = 'None'
    print(item_shipping)
    try:
        item_link = items.find('a', class_='s-item__link')['href']
    except Exception as e:
        item_link = 'None'
    print(item_link)
    print()
