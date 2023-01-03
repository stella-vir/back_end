const te = require('tradingeconomics')
te.login('');
/*
mex = te.getIndicatorData(country='mexico', indicators='gdp').then(function(data) {
	// console.log(data)
});
*/

/*
data = te.getAllCountries().then(function(data) {
	console.log(data)
});
*/

data = te.getFinancialsData(symbol='tsla:us', output_type='df').then(function(data) {
	console.log(data)
});
