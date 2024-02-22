try:
    num = int(input("숫자를 입력하세요:"))
    print(f"{10 / num}입니다")
except ValueError:
    print("숫자가 아님!")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
else:
    print("에러가 안났으니 한잔해")
finally:
    print("에러가 나든 안나든 모르겠다")

try:
    num = int(input("숫자를 입력하세요:"))
    print(f"{10 / num}입니다")
except Exception as e:
    print("에러 발생")



