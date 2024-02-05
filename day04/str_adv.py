# str_adv
# num, str, bool, list
# 문자열 연산자
# +: 연겨 연산자
# *: 반복 연산자
# "ice"[0] => "i": 인덱싱 연산자
# "americano" [0:5]: 슬라이싱 연산자
# in: "ice" in "ice americano": in 연산자

# len(): 길이 구해줌 [문자] 문자 길이 [리스트] 요소갯수
a = len("dslkfjeriofjaoif") # length()
print(a)

test = "americano".upper()
print(test)

test = "americano".replace("cano","car")
print(test)

a = "사과, 바나나, 체리".split(',') #문자 -> 리스트
b = list("사과,바나나,체리")
c = "사과, 바나나, 체리".split(', ')
print(c)

d = ",".join(['a','b','c','d']) # join 리스트 -> 문자
print(d)

# 유저한테 문자를 입력받고
# 단어 사이에 !를 넣는 프로그램 만들기
# ice -> i!c!e

word = input("단어 입력:")
result = "!".join(word)
print(result)

# is ~~니?
"a".isdigit() # 숫자니?
"b".isdigit() # 숫자 or 문자니?
"c".islower() # 소문자니?
"d".isupper() # 대문자니?




