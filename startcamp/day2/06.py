# 함수
# print()
# len()
# range()...

# 함수 정의
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야한다.

# def funcname(parameter_list):
#     """
#     docstring == 함수의 설명서
#     """
#     code

def mul(a, b):
    result = a + b
    return result # 반환 값 없을 시 None출력, 이후 코드가 있더라도 return 까지만 실행

# ex)
# def mul(a, b):
#     result = a + b
#     print(result) print 때문에 출력은 되지만 저장하는 변수에는 None 값 저장
#     None 반환
    
# 함수 실행(호출)
print(mul(1,2))

# 함수 실행 결과(return)값 변수에 할당
a = mul(1,2)
print(a)

# 함수 내부 보기
print(help(len)) # help 사용 시 docstring이 출력됨
