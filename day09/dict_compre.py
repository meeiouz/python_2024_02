# dict_compre [kwy, value]
# key name: 추상적, 포괄적 이름이 좋다

coffeeMenu = ['아메리카노', '라떼', '바닐라', '코코아', '민트모카']
coffeePrice = [2.5, 3, 3.5, 3, 4]

# starbucks = list(zip(coffeeMenu, coffePrice))  #zipper
# print(starbucks)
# megacoffee = dict(zip(coffeeMenu, coffePrice))
# print(starbucks)
# print(megacoffee)

starbucks = [{'name': m, 'price': p} for m, p in zip(coffeeMenu, coffeePrice)]
print(starbucks)

travelList = ['후쿠오카', '오사카', '도쿄', '삿포로', '오키나와']
planePrice = [30, 40, 45, 50, 40]
japan = [{'destination': t, 'price': p} for t, p in zip(travelList, planePrice)]
print(japan)

menu = ['americano', 'latte', 'mint', 'hotchoco']
a = [{'name': i, 'wordLen': len(i)} for i in menu]
print(a)




