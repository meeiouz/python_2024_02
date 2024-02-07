# control_statement(제어문)
# 조건문(Conditional Statements)
# - if, dict
# 반복문(Looping Statements)
# - for, while

# if 조건
num = int(input("정수 입력: "))

if num > 0:
    print("양수입니다.")
print("프로그램 끝")

# 유저에게 문자를 입력 받고, 문자 길이가 10글자 이상이면
# 너무 길어요!, 프로그램 끝
# 프로그램 끝
word = input("문자 입력:")
if len(word) >= 10:
    print("너무 길어요")

# 문자를 입력 받고, 5글자 이상이면서 마지막 문자가 대문자이면 통과! 프로그램 끝
word1 = input("문자 입력:")
if len(word1) >= 5 and word1[-1].isupper():
    print("통과!")

num = int(input("정수 입력:"))
if num > 0:
    print("양수입니다.")
else:
    print("음수 또는 0입니다.")
print("끝")

# 수를 입력하고 홀수인지 짝수인지 구분하는 프로그램
num1 = int(input("숫자 입력하기:"))
if num1 % 2 == 1:
    print("홀수입니다")
else:
    print("짝수입니다")

# 알파벳을 입력하고 알파벳 길이가 홀수인지 짝수인지 구분하는 프로그램
word2 = input("단어 입력:")
if len(word2) % 2 == 1:
    print("홀수입니다")
else:
    print("짝수입니다")

# 알파벳 하나 입력했을 때 대문자인지 소문자인지 구분하는 프로그램
a = input("알파벳 입력:")
if a.isupper():
    print("대문자입니다")
else:
    print("소문자입니다")


num2 = int(input("정수 입력:"))

if num2 > 0:
    print("양수입니다")
elif num == 0:
    print("0입니다")
else:
    print("음수입니다")

# 수학 점수 입력 -> 90이상 a, 80이상 b, 70이상 c, 그 미만 미소
score = input("점수 입력:")

if score >= 90:
    print('a')
elif score >= 80:
    print('b')
elif score >= 70:
    print('c')
else:
    print("미소")

# 각 0~180도 사이의 값을 입력 받고
# 90도 보다 낮으면 예각
# 90도 직각
# 90도 보다 크면 둔각
# 180도 평각
angle = input("각 입력:")

if 0 < angle and angle < 90:
    print("예각")
elif angle == 90:
    print("직각")
elif 90 < angle and angle < 180:
    print("둔각")
elif angle == 180:
    print("평각")
else:
    print("각 입력 오류")

# if 중첩문
if Ture:
    if Ture:
        print("실행")
    else:
        print("안됨")
else:
    print("안됨")

# 단어를 입력받고 단어 길이가 홀수 / 짝수 구분해주고
# 단어에 'a'가 포함되어있으면 'a'를 포함한 홀수/ 짝수네요
# 단어에 'a'가 포함되어있지 않으면 홀수 / 짝수네요
word5 = input("단어 입력:")

if len(word5) % 2 == 0:
    if word5.count('a') > 0:
        print("0을 포함한 짝수입니다")
    else:
        print("짝수입니다")
else:
    if word5.count('a') > 0:
        print("0을 포함한 홀수입니다")
    else:
        print("홀수입니다")
    
