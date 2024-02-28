import random

import pandas
import faker
fake = faker.Faker()


# cgv 일일 매출표
# 손님 이름
# 성별
# 구매한 영화
# 구매한 스낵

cgvData = {
    'customer': [fake.name() for i in range(100)],
    'gender': [random.choice(['남','여']) for i in range(100)],
    'movie': [random.choice(['듄','파묘','웡카']) for i in range(100)],
    'snack': [random.choice(['팝콘', '오징어', '콜라']) for i in range(100)]
}

df = pandas.DataFrame(cgvData)
df.to_csv('cgv.csv', index=False,encoding="utf-8-sig")