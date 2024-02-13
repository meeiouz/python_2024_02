# 1. 유저에게 난이도 고르기 (쉬움, 보통, 어려움)
# 2. 난이도에 따라서
#    -1) 쉬움 0 ~ 100, 보통 0 ~ 1000, 어려움 0 ~ 10000 랜덤 숫자 뽑기
# 3. 유저가 입력한 정수가 랜덤 숫자보다 낮으면 up, 높으면 down, 맞추면 정답!
# 4. 기회는 총 6번 안에 진행되면 계속 맞추기, 넘으면 game over
import random

difficulty = int(input("난이도를 고르세요.(1. 쉬움 2. 보통 3. 어려움):"))
randomNumber = {
    1: random.randint(0,101,),
    2: random.randint(0,1001,),
    3: random.randint(0,10001,),
}
answer = randomNumber[difficulty]
life = 0

while life < 6:
    user = int(input("정답을 입력하세요:"))
    if answer == user:
        print("정답입니다")
        break
    else:
        if answer > user:
            print("up")
        else:
            print("down")
        life += 1

if life == 6:
    print("game over")
    print(f"정답은 {answer}입니다")
else:
    print("승리하셨습니다")
