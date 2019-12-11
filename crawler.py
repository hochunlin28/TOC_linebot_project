import requests
from bs4 import BeautifulSoup
import random


def crawl_img():
    num = random.randint(1,300)
    url = "https://memes.tw/wtf?sort=hot&page="+str(num)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    array = soup.find_all('img',{'class': 'img-fluid lazy'})
    
    rand = random.randint(0,len(array)-1)
    
    """
    for img in array:
        print(img)
    """
    


    #while array[rand].find('img',class_='img_fluid lazy') == None:
    #rand = random.randint(0,len(array)-1)
    #print(array[rand])
    
    print(array[rand]['data-src'])
    return array[rand]['data-src']

    

