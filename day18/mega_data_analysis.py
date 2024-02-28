import pandas

mega = pandas.read_csv('mega.csv')
print(mega.index)
print(mega.columns)
print(mega['customer'])
print(mega.iloc[500])
print(mega[mega['coffee']=='딸기라떼'])
print(mega[mega['pay']=='체크카드'])


group_by_pay = mega.groupby('pay')
print(group_by_pay['coffee'].value_counts())


# 커피를 그룹핑 해서 나이대별로 산출
group_by_coffee = mega.groupby('coffee')
print(group_by_coffee['apges'].value_counts())

# 나이를 그룹핑 해서 커피별로 산출
group_by_ages = mega.groupby('ages')
print(group_by_ages['coffee'].value_counts())

# 시간대별로 그룹핑 해서 나이대별로 산출
group_by_time = mega.groupby('time')
print(group_by_time['ages'].value_counts())

# 시간대별로 그룹핑 해서 커피 산출
group_by_time = mega.groupby('time')
print(group_by_time['coffee'].value_counts())

# 지불수단별로 그룹핑 해서 시간대 산출
group_by_pay = mega.groupby('pay')
print(group_by_pay['time'].value_counts())

# 커피를 그룹핑 해서 나이대 별로 선출하고 제일 인기 있는 것만 보여주기
# .groupby(level=0).head(1): 1순위만 보여주기
print(group_by_coffee['ages'].value_counts().groupby(level=0).head(1))


