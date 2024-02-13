# 0~ 100까지의 짝수를 출력하기
for x in range(101):
    if x % 2 == 0:
        print(x)

# 유저에게 정수를 입력받고, 해당 정수의 구구단 출력하기
num = int(input("정수 입력:"))
for x in range(1,10):
    print(f"{num} *{x} = {num * x}")

# 랜덤으로 0~10000까지의 숫자를 뽑아서, 10개를 리스트에 넣고
# 오름차순으로 출력하고, 각 요소의 총합을 구하기
import random

numlist = []
for x in range(10):
    numlist.append(random.randint(0,10001))
numlist.sort()
print(numlist)
print(sum(numlist))
#total = 0
# for x in numlist:
#total += 1

