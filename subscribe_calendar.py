import tradingeconomics as te
import json

# te.login('guest:guest')
te.login('5b47a77efd37439:5kzkij2hyxd98d4')

def on_message(ws, message):
    print(json.loads(message))

'''
web socket
te.subscribe('EURUSD:CUR')

te.subscribe('calendar')
te.subscribe('news')

te.run(on_message)
'''

se = te.getSearch(output_type='df')
se = te.getSearch()

gold = te.getSearch(term = 'gold')

euro = te.getEurostatData(lists='categories')

po = te.getEurostatData(category_group='Poverty')

wb = te.getWBCategories(category='Science & Technology')

comtrade = te.getCmtCategories()

com_upt = te.getCmtUpdates()

type = te.getCmtTotalByType(country='sweden', type='export')

imp = te.getCmtTotalByTypeAndMainCategory(country='sweden', type='import')

fed = te.getFedRStates()

county = te.getFedRStates(county='Iowa')

snap = te.getFedRSnaps(country='united states')

state = te.getFedRCounty(state='california')

disparity = te.getHistorical('racedisparity005007:fred')

print(disparity)







# end
