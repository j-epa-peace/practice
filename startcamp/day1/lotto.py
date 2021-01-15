import random

numbers = range(1,46)

pick = random.sample(numbers, 6)
print(f'오늘의 로또 번호는 {pick}입니다')
