class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"브랜드: {self.brand} 모델: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine
    def info(self):
        self.display_info()
        print(f"engine: {self.engine}")

a = Car("벤츠","e클래스","V8")
a.info()

# 몬스터 클래스
# 체력, 공격력
# 때리기
class Monster:
    def __init__(self, hp, attack):
        self.hp =hp
        self.attack = attack

    def hit(self):
        print(f"{self.attack} 데미지 입힙니다.")

# slime: 방어하기 함수[체력을 안깍임]
class Slime(Monster):
    def __init__(self, hp, attack):
        super().__init__(hp,attack)
    def defense(self):
        print("체력이 안깍임")

# pig: 돌진하기 함수[공격력의 2배 데미지 입힘]
class Pig(Monster):
    def __init__(self, hp, attack):
        super().__init__(hp, attack)
    def rush(self):
        print(f"공격력 {self.attack * 2}입힘")

# witch: 속성 분노, 분노하기 함수[분노가 오름], 급발진 함수[공격력의 5배 데미지]
class Witch(Monster):
    def __init__(self, hp, attack):
        super().__init__(hp, attack)
        self.range = 0
    def reiseRange(self):
        self.rage += 10
    def suddenRange(self):
        print(f"공격력 {self.attack * 5}입힘")



