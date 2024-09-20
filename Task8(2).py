'''Task 8b : url = 'https://books.toscrape.com/'

price, title, rating in csv of all book of page1'''



import requests as rq
import pandas as pd
from bs4 import BeautifulSoup

url='https://books.toscrape.com/'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
response=rq.get(url=url,headers=header)
bsoup=BeautifulSoup(response.content,"html.parser")

qdata=bsoup.findAll('article',class_='product_pod')

data=[]
for item in qdata:
    title = item.h3.a['title']
    price = item.find('p',class_='price_color').text
    rating = item.p['class'][1]

    Booksdata={
        'title':title,
        'price':price,
        'rating':rating
    }
    data.append(Booksdata)

print(data)
qpandas=pd.DataFrame(data)
qpandas.to_csv('Allbooks.csv')