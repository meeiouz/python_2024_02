import random

# randint(start,and): 임의의 정수 뽑기
print(random.randint(0,10)) # 0~10 사이의 정수를 뽑기

# choice([]): 리스트에서 임의로 뽑기
print(random.choice(["엄마는 외계인", "뉴욕치즈케이크","민초"]))

#random(): 0과 1 사이의 실수
print(random.random())

# suffle(): 리스트 섞기
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)