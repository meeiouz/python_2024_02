import pandas
import faker
import random
fake = faker.Faker('ko_KR')

ageList = ['10대', '20대', '30대', '40대', '50대', '60대']
ageWeight = [20,30,30,10,5,5]
coffeeList = ['아아', '따아', '아라', '따라', '딸기라떼', '바닐라라뗴','민트라뗴']
coffeeWeight = [30,10,10,10,20,10,10]
payList = ['현금', '체크카드', '신용카드', '카카오페이', '티머니']
payWeight = [5, 40, 40, 10, 5]
time = ['아침', '점심', '저녁', '밤']
timeWeight = [60, 50, 30, 10]

mega = {
    'customer': [fake.name() for i in range(1000)],
    'ages': [random.choices(ageList, weights=ageWeight, k=1)[0]for i in range(1000)],
    'coffee': [random.choices(coffeeList, weights=coffeeWeight, k=1)[0] for i in range(1000)],
    'pay': [random.choices(payList, weights=payWeight, k=1)[0] for i in range(1000)],
    'time': [random.choices(time, weights=timeWeight, k=1)[0] for i in range(1000)],
}

df = pandas.DataFrame(mega)
df.to_csv('mega.csv',index=False,encoding='utf-8-sig')