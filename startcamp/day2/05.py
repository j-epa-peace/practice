# 조건문

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드

# n = 11

# if n % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

# 반복문
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 리스트의 원소중 홀수만 찾아라

for number in numbers: # for 문 원소 찾을 때 단수형으로 써줘서 이쁘게 만듬.
    if number % 2 == 1:
        print(f'{number}는 홀수입니다', end = 'd\n')
    else:
        print(f'{number}는 짝수입니다')

