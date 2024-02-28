# 2호선별로 그룹핑

import pandas

subway = pandas.read_csv('subway.csv')
lines = subway.groupby('노선명')
station = lines['역명'].value_counts()

# 승차총승객수 그룹핑하고 역명 나타내기
guest = subway.groupby('승차총승객수')
station_with_guest = guest['역명'].value_counts()
print(station_with_guest)