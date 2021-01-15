import requests
from bs4 import BeautifulSoup
url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
key = '#exchangeList > li.on > a.head.usd > div > span.value'
result = data.select_one(key).text
print(result)


