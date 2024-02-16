# verb(): 함수[input & output like 마술 상자]
# print(), input(), int(), str(), bool()

def add(a, b):
    return a + b


c = add(10, 20)
print(c)


def giveEgg():
    return '👻👻👻👻👻👻'


a = giveEgg()
print(a)


def fry(x):
    if x == '🥚':
        return '🍳'
    else:
        return '?'


print(fry('a'))


def zodiac(year):
    zodiac = year % 12
    animal = {

        0: '🐵',
        1: '🐔',
        2: '🐶',
        3: '🐷',
        4: '🐭',
        5: '🐮',
        6: '🐯',
        7: '🐰',
        8: '🐲',
        9: '🐍',
        10: '🐴',
        11: '🐑',
    }
    return animal[zodiac]
print(zodiac(2004))


