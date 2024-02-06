# dict
# key_value, key(고유, only-one)
# key: int, str
# value: 다 됨

issac = {
    'ham': 2500,
    "cheese": 3000,
    "bacon": 3000,
}
print(f"{issac['ham']}")

bong = {
    'eggham': 3800,
    "soya": 3200,
    "original": 3000,
}

cgv = {
    'popcorn':['소금', '카라멜', '어니언'],
    'beverage': {
        'sprite': 2000,
        'zero_coke': 1500,
    }
}
print(f"{cgv['popcorn'][0]}")
print(f"{cgv['beverage']['zero_coke']}")

mbti = {
    'e': '외향적',
    'i': '내향적',
    's': '현실적',
    'n': '미래지향적',
    'f': '감성적',
    't': '이성적',
    'p': '즉흥적',
    'j': '계획적',
}
a = input("당신의 mbti는?")
print(f"당신은 {mbti[a[0]]}, {mbti[a[1]]}, {mbti[a[2]]}, {mbti[a[3]]}입니다 ")
