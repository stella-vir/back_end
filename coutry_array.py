import tradingeconomics as te
from datetime import datetime
import time
import pandas as pd

te.login('5b47a77efd37439:5kzkij2hyxd98d4')

countries = ['mexico', 'sweden']
indicators = ['GDP', 'interest rate']

today = datetime.now().strftime('%Y-%m-%d')

def step(years, n):
    for i in range(0, len(years), n):
        yield years[i:i+n]


for c in step(countries, 1):
    print(c)

data = te.getFinancialsData(symbol='tsla:us', output_type='df')
path_csv = r'data.csv'
path_html = r'data.html'
data.to_csv(path_csv, index=False, header=True, sep='|')
data = data.astype(str)
data.round(5)
data.to_html(path_html)













# end
