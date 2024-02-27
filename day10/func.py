# 함수[function]: (마술 상자) [input[None] & output[None]]
# [내장[파이썬, 표준] 함수]print(), input(), int(), str(), bool(), len(), sum(), enumerate()
# [문자열 함수] "abc".upper(), "abc".isUpper, "abc".count('a')...

# 함수 정의
def add(a,b):
    return a+b

# substract, multiply 함수
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b

#'🥚'
# makeTofry 계란이모지 -> 후라이/다른거 -> ?
def makeTofry(x):
    if x == '🥚':
        return '🍳'
    else:
        return '?'

a = makeTofry('🥚')
print(a)

# def bank
# 농협은행 -> 넘이쁘네, 기업은행 -> 귀여운데, 국민은행 -> 고민해, 신한은행 -> 신나네, 그 외 -> ?
def bank(x):
    bankName = {
        '농협은행': '넘이쁘네',
        '기업은행': '귀여운데',
        '국민은행': '고민해',
        '신한은행': '신나네',
    }
    return bankName.get(x, '?')
print(bank('신한은'))

# 가변 매개변수
def makePizza(*topping):
    print("피자 오지게 굽는중")
    for i in topping:
        print(f"추가되는 토핑:{i}")

makePizza('치즈', '버섯', '올리브', '페퍼로니')

#zoodiac 띠 구하기
#def zodiac(*arg) [1996 ~ 2005]
#zoodiac(1996, 2000, 2005) -> 쥐, 용, 닭

def zodiac(*year):
    zodiacDict = {
        1996: '쥐',
        1997: '소',
        1998: '호랑이',
        1999: '토끼',
        2000: '용',
        2001: '뱀',
        2002: '말',
        2003: '양',
        2004: '원숭이',
        2005: '닭',
        2006: '개',
        2007: '돼지',
    }
    for i in year:
        print(f"{zodiacDict[i]}")

    zodiac(1999, 2000, 2001, 2002, 2005)

# 자연수 n이 매개변수로 들어오면, 배열화시키고 반대로 나타내기
# 12345 -> [5,4,3,2,1]
# 8974 -> [4,7,9,8]

def numberReverse(n):
    numlist = list(str(n)) #"[1,2,3,4,5]"
    numlist.reverse()
    return [int(i) for i in numlist]
print(numberReverse(12345))