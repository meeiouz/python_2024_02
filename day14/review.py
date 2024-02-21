# class = 변수 + 함수

class Restaurant:
    def __init__(self,a):
        self.name = a
        self.menu = []

    def showMenu(self):
        print(f"가게이름:{self.name} 메뉴: {self.menu}")

    def addMenu(self):
        food = input("추가할 메뉴:")
        self.menu.append(food)

# a = Restaurant("김밥")
# a.addMenu()
# a.addMenu()
# a.showMenu()
# b = Restaurant("이삭")
# b.addMenu()
# b.showMenu()

# 카페 클래스
# 변수[속성]: 카페 이름, 커피 메뉴[{'name':'americano','price':3000}], 알바생 목록, 매출
# 함수[동작]: 커피 추가, 알바 고용하기, 커피 판매

class Cafe:
    def __init__(self,a):
        self.name = a
        self.menu = []
        self.worker = []
        self.sales = 0

    def addCoffee(self):
        name = input("커피 이름:")
        price = int(input("커피 가격:"))
        self.menu.append({'name': name, 'price': price})

    def hireWorker(self):
        worker = input("직원 이름")
        self.worker.append(worker)

    def showInfo(self):
        print(f"카페 이름:{self.name}, 커피 메뉴:{self.menu}, 알바생:{self.worker} 매출:{self.sales}")

    def sellCoffee(self):
        num = int(input(f"{self.menu}중에서 번호를 고르세요:"))
        self.sales += self.menu[num]['price']



t = Cafe("투썸")
t.addCoffee()
t.addCoffee()
t.sellCoffee()
t.sellCoffee()
t.showInfo()



