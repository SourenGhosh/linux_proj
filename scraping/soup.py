import requests
from bs4 import BeautifulSoup
for i in range(20):
    URL = 'https://www.carandbike.com/new-bikes/models?q=%2Fnew-bikes%2Fmodels&newbike-page=' + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('figcaption', class_='newmodel-bike_ttl')
    f  = open("am2.text", 'w')
    f.write(soup.text)
    f.close()