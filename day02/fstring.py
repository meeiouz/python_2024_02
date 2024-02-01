#variable - 변수[기억하는 곳]
#변수 이름 짓는 문법
#1. 영어, 숫자, 특수문자(_) 사용하기
#2. 대소문자를 구별함 ex) A, a 다름
#3. 띄어쓰기 안된 ex) my_name 안됨 -> my_name 또는 myname
#4. 숫자로 시작 불가능 ex) 1a 안됨 a1은 됨

# 변수 이름 짓는 국룰
#1. 변수명은 의미 있는 것으로 짓기
#2. 두 단어가 모여서 이름 지을 떄
# -1) camelCase -> megaStudy: 두 번쨰 단어 뒤부터 대문자 시작
# -2) snakeCase -> meda_study
#3. 소문자 시작

my_age = "21"
my_name = input("당신의 이름은: ")

print(f"안녕하세요 저의 이름은 {my_name}입니다.")
