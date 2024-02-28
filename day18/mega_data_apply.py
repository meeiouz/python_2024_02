import pandas

mega = pandas.read_csv('mega.csv')

def event(row):
    if row['ages'] == '50' or row['ages'] == '60':
        return "할인 대상"
    else:
        return "할인 대상 아님"

mega["어르신 이벤트"] =  mega.apply(event,axis=1)
print(mega)


def event2(row):
    if row['pay'] == '티머니' and row['ages'] == 20:
        return "할인 대상"
    else:
        return  "할인 대상 아님"

mega['티머니 이벤트'] = mega.apply(event,axis=1)