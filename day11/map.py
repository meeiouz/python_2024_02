a = [2, 3, 4, 5, 6]
res = map(lambda x: x*2,a) # 어떠한 타겟을 바꾸기
print(list(res))

res1 = map(lambda x: x**2,a)
print(list(res1))

eggs = ['🥚', '🥚', '🥚']
chicks = map(lambda x: '🐥',eggs)
print(list(chicks))

chickens = map(lambda x: '🐓',eggs)
print(list(chickens))


import random
def hatchEggs(x):
    a = ['🐣' if i <= 30 else j for i,j in enumerate(x)]
    random.shuffle(a)
    return a

hatchEggs(eggs)
result = map(hatchEggs, eggs)
print(list(result))

