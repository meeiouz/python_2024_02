# [표현식 for 항목 in 반복가능객체(리스트, 문자열, range...)]
# [i for i in range(100)]
# [1 for i in range(100)]

# a = [i + 10 for i in [1, 2, 3]]
# print(a)

# 2, 조건문(filter)
a = [i for i in range(100) if i % 2 == 0]
print(a)

b = [i for i in range(10000) if i % 15 == 0]
print(b)

cholist = ['Ghana', 'godive', 'hershey', 'Royce']
print([len(i) for i in cholist])

c = [len(i) for i in cholist if len(i) % 2 == 0]
print(c)

d = [i for i in cholist if 'e' in i]
print(d)

# 3. 조건문(치환)
e = [i if i % 2 == 0 else '♡' for i in range(101)]
print(e)

f = ['☆' if i % 3 == 0 else '♡' for i in range(101)]
print(f)

# a 포함이면 ♧ 아니면 문자길이로 치환
g = ['♧' if 'a' in i else len(i) for i in cholist]
print(g)

# 369게임
# 1 ~ 100 출력을 하는데, 3,6,9가 포함되어있으면 '♤'
# 아니면 그대로 출력
h = ['♤' if str(i % 10) in '369' or str(i // 10) in '369' else i for i in range(1, 101)]
print(h)

# 4. 중첩 루프 컴프리헨션

print([(i,j) for i in range(10) for j in range(10)])
print([f"{i} * {j} = {i * j}" for i in range(1, 10) for j in range(1, 10)])








