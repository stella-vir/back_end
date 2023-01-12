import tradingeconomics as te
from decimal import Decimal

te.login('op54h7t3vb4qqfw:y07h89iukk27jwe')

data = te.getHistorical(symbol='aapl:us', output_type='df')
print(type(data))


data['Symbol'] = data['Symbol'].str.lower()

print(type(data['Date'][1]))


def cast(str):

    split = str.split('/')
    # print(split)

    concat = split[2] + '-' +  split[1] + '-' + split[0]

    return concat

def dec(no):
    print(type(no))
    no = Decimal(no)
    no = "{:.1f}".format(no)

    return no

for i, row in data.iterrows():
    data._set_value(i,'Date',cast(row['Date']))
    data._set_value(i,'Close',dec(row['Close']))


print(data)











# end
