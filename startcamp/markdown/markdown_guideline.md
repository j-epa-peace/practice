# headings

mark up (생산, 빌드, 정리해서 만듦) vs 마크 다운 (마크업에 대비해서 나옴. )

## 두번쨰로 작은거 ##

### --- 이거는 줄치기



정리를 위한 앱!

- 워드 : 텍스트는 정리 가능한데 코드는 정리불가. 그래서 코드블럭 제공이 필요했음.
- 코드 주석.

```python
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
```

## 2. list

- 그냥 - 이걸로 만들어줌.
- ㅁㄴㄹ
  - ㅁㄴㅁㅇ
    - ㄹㄴ
      - 계속 tab으로 만들어 줌.

1. 순서가 있는 경우
2. 그냥 숫자만

## 3. backquote ```면 code block.  

## `면 인라인 블럭

```python
print('hello')
```

` 인라인 블럭` 

## 4. image 삽입 가능

- local의 의미 (컴퓨터 안에 있다.) <-> online (인터넷 환경에 있는거)
- 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 이미지를 출력

![사슴](https://post-phinf.pstatic.net/MjAxODEyMjZfMjY5/MDAxNTQ1ODA5OTg2MjU5.fB8mb5wDo84uztMAGYGrOHfcTxL8-NcmqaoomM7BmSgg.o-wdtnhWUzDIkJCQsPzCT5ZWrTPYdhlIcOeXVE2SJsIg.JPEG/2.jpg?type=w1200)

로컬에 있는 경우는 드래그 앤 드랍으로 넣어줄 수 있는데 넣게 되면 폴더 하나 새로 만들어줌!



## table ctrl + t

| 엑셀처럼 자유롭진 않아                          |    ㅇㄴㅍㅋㅍㅋㅊㅌㅍㅌㅋ    | ㅌㅊㅋㅍㅋㅌㅊㅍㅋㅌㅊㅍㅊㅌㅋ |
| :---------------------------------------------- | :--------------------------: | ------------------------------ |
| 색깔 안되고, 셀 병합 같은 건 안되구 정렬은 된다 | ㅌㅊㅋㅍㅌㅋㅍㅌㅋㅍㅌㅋㅊㅍ | ㅌㅊㅋㅍㅋㅌㅊㅍㅌㅋㅍ         |
|                                                 |                              |                                |
|                                                 |                              |                                |

## 인용문 >

> 해보기
>
> > 이ㅏㄴㅁㅣ

마크다운 가이드 숙제~



# Git



## Git 개념

git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.



## Git 설정

`전역 영역`에서 commit 기록의 주인을 등록

``` python
$ git config --global user.name "username"
$ git config --global user.email "edu@hphk.kr"
```



## Git 기본

- git init 해당 디렉토리를 Git이 관리하도록 초기화
- add 파일명 커밋할 목록에 추가
- commit -, "커밋 메시지" (히스토리의 한 단위) 만들기
- git push origin master 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋 반영



## Git 저장소

| 로컬(working directory) | staging area -           | remote repository(github, bitbucket, gitlab) |
| ----------------------- | ------------------------ | -------------------------------------------- |
| 로컬 컴퓨터 저장소      | 해당 버전의 스냅샷(기록) | 원격 저장소                                  |



## Git branch

__같은 작업물을 기반으로 동시에 다양한 작업을 할 수 있게 만들어 주는 기능__

독립적인 작업 영역 안에서 마음대로 소스코드를 변경할 수 있다. 분리된 작업 영역에서 변경된 내용은 추후에 기존 버전과 비교해서 새로운 하나의 버전을 만들어 낼 수  있다.