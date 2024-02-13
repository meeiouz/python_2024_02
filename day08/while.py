# 반복문: for, while

a = 1
while a < 5:
    print("설날 끝나서 현타 개온다.")
    a += 1

while True:
    num = int(input("정수 0을 넣으면 끝남:"))
    if num == 0:
        break

# while문을 사용해서 1~10까지 더한 값을 출력하는 코드
b = 1
total = 0
while b < 11:
    total += b
    b += 1
print(total)

# 유저에게 어떤 정수 n을 입력받고
# while 무한루프에서 정수 n을 입력받으면 탈출하는 코드 만들기
n = int(input("정수 입력:"))
while True:
    m = int(input("루프 안에서 정수 입력:"))
    if n == m:
        break

# 랜덤으로 0~10가지 아무 숫자를 뽑고
# 유저에게 해당 숫자를 맞추게 하는 게임
# 맞추면 정답입니다. 하고 끝
# 틀리면 틀렸습니다. 다시 입력하세요.
import random
c = int(input("정수 입력:"))
for x in range(0,11):
    while True:
        if c == x:
            print("정답입니다")
            break
        else:
            print("틀렸습니다")
            break

import random
 answer = random.randint(0,11)

 while True:
     a = int(input("정답을 맞춰보세요"))
     if answer == a:
         print("정답입니다")
         break
        else:
            print("틀렸습니다. 다시 시도하세요")
print("끝")



