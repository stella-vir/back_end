import tradingeconomics as te
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

te.login('5b47a77efd37439:5kzkij2hyxd98d4')

def compare(date, diff):
    date = datetime.strptime(str(date), '%Y-%m-%d').date()
    date1 = str(date)
    date2 = str(date + relativedelta(years=diff))
    return date2

def comp(country=None, indicator=None, initDate=None, endDate=None):
    data = te.getHistoricalData(country=country, indicator=indicator,
    initDate=initDate, endDate=endDate, output_type='raw')

    data1 = list(filter(lambda x:True if x['DateTime'] >= initDate
    and x['DateTime'] <= endDate else False, data))
    data2 = list(filter(lambda x:True if x['DateTime'] >= endDate else False, data))

    # return data
    return [pd.DataFrame(data1), pd.DataFrame(data2)]

print(compare('2022-01-01', 1))
print(comp(country='mexico', indicator='currency',
initDate='2019-01-01', endDate=compare('2019-01-01', 2)))




# end
