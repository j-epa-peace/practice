import requests
from pprint import pprint

#request paramet 들은 ? 다음에 나옴.
key = 'ffApqI9Ep1ri%2BOYGxOXEPrtxmF7IvOZrDcVhgsX1fm12dQL3qW%2FbTHhPeIqojbFRq9HAbWswn%2BVOaUcQIwZStg%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sidoName = '서울'
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sidoName}&ver={ver}'

response = requests.get(url).json()

# print(response) 더러워서 이쁘게 만드려면
# pprint 사용 내장함수인데 불러와야함
#pprint(response)

# station의 미세먼지 농도는 pm10Value입니다.

station = response['response']['body']['items'][0]['stationName']
dust = response['response']['body']['items'][0]['pm10Value']

print(f'{station}의 미세먼지 농도는 {dust}입니다')

#return 값이 있어야지 만 f-string 에 쓸 수 있음. index로는 사용못함.
