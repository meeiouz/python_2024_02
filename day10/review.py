# 1.리스트 컴프리헨션 필터링
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

newWords = [i for i in words if 'a' in i and len(i) > 5]
print(newWords)

# 2. 리스트 컴프리헨션 필터링 (숫자)
numbers = [30, 55, 20, 75, 40, 90, 10, 65]
newNumbers = [i for i in numbers if i > 50]
print(newNumbers)


names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
firstName = [j for i,j in enumerate(names) if i % 5 == 0]
print(firstName)

# 3. 두 정수 덧셈 또는 뺄셈