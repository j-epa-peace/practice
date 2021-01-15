import requests # 짧은 거부터 써주기
from bs4 import BeautifulSoup

# 1. 주소
url = 'https://finance.naver.com/sise/'

# 2. url 로 요청을 보낸다.
response = requests.get(url).text

# 3. 받은 응답을 예쁘게 꾸며준다. beautifulSoup
data = BeautifulSoup(response, 'html.parser')
#print(data) # chrome 개발자 모드에서 볼 수 있는 내용

# 4. 꾸민 응답중에서 원하는 데이터를 선택. select & select_one
result = data.select_one('#KOSPI_now').text # copy selector 로 저장한 값
print(result)
