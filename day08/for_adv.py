fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]

# enumerate(): 번째, 요소 출력
for i,j in enumerate(fruits):
    print(f"{i}번째 {j}")

for i,j in enumerate(fruits):
    if not j.count('a') > 0:
        print(i)

# 리스트 컴프리헨션
# [i for i in range()]

a = [i for i in range(11)]
b = [i + 10 for i in range(11)]
c = [i ** 2 for i in range(11)]
fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
d = [i.upper() for i in fruits]
print(d)


