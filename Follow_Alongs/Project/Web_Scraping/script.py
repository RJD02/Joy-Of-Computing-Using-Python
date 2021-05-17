from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import sys

driver = webdriver.Chrome('D:\\chromedriver_win32\\chromedriver')

products = []
prices = []
ratings = []
# defaultUrl = "https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=b49611cd-5f21-4e00-a591-13ff06c67f1e"
url = sys.argv[0]
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('div', attrs={'class': '_2kHMtA'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    try:
        if(name.text and price.text and rating.text):
            products.append(name.text)
            prices.append(price.text)
            ratings.append(rating.text)
            print(name.text)
            print(price.text)
            print(rating.text)
            print('Not formatted')
    except:
        print('skipped')

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('laptops.csv', index=False, encoding='utf-8')
