# 조건문[if]: 조건에 따라 코드 실행
# 반복문[for]: 코드를 n번 실행
import random

# range(n): 0~n-1까지 반복해주는 기능
# range(start,end)
for x in range(51):
    print(x)
for x in range(10,51):
    print(x)

a = []
for x in range(100):
    a.append(x)
print(a)

import random

for x in range(30):
    a.append(random.randint(0,10000))
a.sort()
print(a)

a = []
for x in range(101):
    if x % 2 == 0:
        a.append(x)
print(a)

a = []
for x in range(101):
    if x % 3 == 0 and x % 5 == 0:
        a.append(x)
print(a)

# for "문자열", 리스트

for x in "megastudy":
    print(x)

for x in ['☆', '♧', '♡']:
    print(x)

# 구구단 출력
# 정수를 입력하면
# ex)3 -> 3 * 1 = 3, 3 * 2 =6, 3 * 3 = 9,
num = int(input("정수 입력:"))
for x in range(1,10):
    print(f"{num} * {x} = {num * x} ")


# 리스트에서 짝수들의 합을 구하기
# ex) 랜덤(0~1000)으로 10개 뽑고 먼저 출력하고 짝수의 합은 -입니다
