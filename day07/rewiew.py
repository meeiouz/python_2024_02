# 알파벳 탐지기. 소문자 -> 대문자, 대문자 -> 소문자
alpha = input("알파벳 입력:")
if alpha.isupper():
    print(alpha.islower())
else:
    print(alpha.isupper())

# 비밀번호 설정 프로그램
password = input("비밀번호 설정:")

if len(password) < 10:
    print("비밀번호를 10 글자 이상 설정해주세요.")
elif not  "!" in password or "#" in password or "@" in password:
    print("특수문자 !#@를 넣어주세요.")
elif not password[0].isupper():
    print("첫번째 글자는 대문자로 해주세요!")
else:
    print("비밀번호가 설정되었습니다.")

# 버스 요금 계산기
bus_fee = {
    "name": ["시내버스", "광역버스", "마을버스"],
    "fee": [1200, 2000, 1000],
    "age_sidcount": ["어린이 무료", "청소년 1000", "노인 무료"]
}
print(f"{bus_fee['name']} {bus_fee['fee']} 중에 버스를 선택하세요 [{bus_fee['age_discount']}]")
busNumber = int(input("번호 입력:"))
age = int(input("나이 입력:"))

if age <= 7 or age >= 65:
    print("무료입니다")
elif 8 <= age and age <= 19:
    print(f"선택하신 버스의 가격은 {bus_fee['fee'][busNumber] * 0.7}입니다.")
else:
    print(f"선택하신 버스의 가격은 {bus_fee['fee'][busNumber] * 1}입니다.")


