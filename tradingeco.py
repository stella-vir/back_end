import tradingeconomics as te

te.login('5b47a77efd37439:5kzkij2hyxd98d4')


prt = te.getIndicatorData(country=['mexico'], output_type='df')

gdp = te.getIndicatorByCategoryGroup(country='mexico', category_group='gdp', output_type='df')

gdp = te.getIndicatorData(country='mexico', indicators='gdp', output_type='df')

peer = te.getPeers(country='mexico', category='money', output_type='df')

ticker = te.getIndicatorByTicker(ticker='MXONBR', output_type='df')
ticker = te.getIndicatorByTicker(ticker='MXONBR')

his = te.getHistoricalData(country='mexico', indicator='gdp', initDate='2013-01-01')

shis = te.getHistoricalData(country=['sweden', 'mexico'], indicator=['gdp', 'population'], initDate='2013-01-01', endDate='2022-12-31')

ghis = te.getHistorical('MXONBR')

upt = te.getHistoricalUpdates()

dis = te.getDiscontinuedIndicator(country = ['mexico', 'sweden'])

rates = te.getRatings(country=['mexico', 'sweden'])

his_rates = te.getHistoricalRatings(country=['mexico', 'sweden'], initDate='2010-01-01')

lt_upt = te.getLatestUpdates(init_date='2018-01-01')

cal = te.getCalendarData(country=['mexico', 'sweden'], importance='2', category='inflation rate', initDate='2020-01-01')

cal_idx = te.getCalendarData(country='sweden', category='inflation rate', initDate='2017-01-01')

id = te.getCalendarId(id='')

cal_tk = te.getCalendarData(ticker='MXONBR')

com = te.getMarketsData(marketsField='index')

cur = te.getCurrencyCross(cross='')

ins = te.getMarketsBySymbol(symbols='')

mar_peer = te.getMarketsPeers(symbols='tsla:us')

st_ctry = te.getStocksByCountry(country='sweden')

comp = te.getMarketsComponents(symbols='')

desp = te.getMarketsStockDescriptions(symbol='aapl:us')

de_cty = te.getMarketsStockDescriptions(country='sweden')
de_cty1 = te.getMarketsStockDescriptions(country='mexico')

search = te.getMarketsSearch(country='sweden', category=['index', 'markets'])

sym = te.getMarketsSymbology(symbol='tsla:us')

ti = te.getMarketsSymbology(ticker='tsla')

his = te.getHistorical(symbol='')

fetch = te.fetchMarkets(symbol='')

intra = te.getMarketsIntraday(symbols='')


financials = te.getFinancialsData(symbol='SIE:GR')
financials = te.getFinancialsData(symbol='TSLA:US')

earn = te.getEarnings()

forecast = te.getForecastData(country='sweden')

for_data = te.getForecastData(indicator='gdp')

mar_for = te.getMarketsForecasts(category='bond')

mar_sym = te.getMarketsForecasts(symbol='')

news = te.getNews(country='sweden', start_date='2021-01-01')

new_country = te.getNews(country='sweden', indicator='inflation rate')

n_idx = te.getNews(start=10, limit=5)

print(n_idx)







# end
