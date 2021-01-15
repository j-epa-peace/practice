#json javascript obeject notation 
#가장 많이 사용되는 데이터 주고 받는 표기법.
#api application programming interface
#배달의 민족 로그인-> 소셜 로그인 많이 사용.
#전혀 다른 앱인데 다른 앱끼리 소통을 함.
#소통할 때 데이터를 json 문서로 만들어서 보내줌.
#사실 생긴건 json은 딕셔너리 형태인데 javascript에서 이름이 json일 뿐.

import requests

name = 'tom'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
print(response)

# .하고 나오는 것을 method 라 칭함.
# attribute vs method(function) 의 차이. function 이 class 안에 있을 때 method라고 한다.
# attribute 는 속성값이라 하여 함수를 주는게 아니라 그냥 값을 보여줌
# 이런 걸 확인하려면 공식 문서 참조.

age = response['age']

print(f'{name}의 나이는 {age}입니다')