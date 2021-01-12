import requests
import os
from bs4 import BeautifulSoup
img_link = []
for i in range(20):
    URL = 'https://www.carandbike.com/new-bikes/models?q=%2Fnew-bikes%2Fmodels&newbike-page=' + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    image = soup.select('img[src^="https://images.carandbike.com/bike-images/medium/honda"]')
    for ig in image:
        img_link.append(ig['src'])
i=1
for index, link in enumerate(img_link):
    img_data = requests.get(link).content
    with open("bike_photos//"+str(index+1)+'.jpg', 'wb+') as f:
        f.write(img_data)
        f.close()