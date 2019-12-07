import requests
from bs4 import BeautifulSoup
import random


def crawl_img():
    num = random.randint(1,300)
    url = "https://memes.tw/wtf?sort=hot&page="+str(num)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    array = soup.find_all('img')

    rand = random.randint(0,len(array))


    while array[rand]['src'].find("http", 6) != -1:
        rand = random.randint(0,len(array))

    return array[rand]['src']
