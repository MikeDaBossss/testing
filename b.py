import pandas as pd 
import requests
import json
from pandas.io.json import json_normalize
stocklist = pd.read_excel('sp_500_stocks.xlsx')

# print(stocklist['Ticker'][140:143])

# naicscodes = pd.read_csv('naicsCodes.csv')
# print(naicscodes.columns)
# print(naicscodes)
# import chardet
# with open(r'companyProfile.csv','rb') as f:
# 	result = chardet.detect(f.read())
# 	companyprofile = pd.read_csv('companyProfile.csv',encoding=result['encoding'])
# print(result['encoding'])
# print(companyprofile.columns)
# print(companyprofile['sector'].unique())
# #unique = companyprofile['sector']
# conversionlist = [8,8,6,7,1,6,2,1,9,5,7,3,5,6,9,0,2,2,2,4]
# maxcol = 0
# companyprofile['naics'] = "tazo"
# companyprofile['naics1'] = "tazo"
# companyprofile['naics2'] = "tazo"
# companyprofile['naics3'] = "tazo"
# for t,i in enumerate(companyprofile['sector']):
# 	#find the index of company sector in the list of sectors
# 	ind = list(companyprofile['sector'].unique()).index(i)
# 	#find the indexes in conversionlist where the above index is present
# 	x = [c for c,x in enumerate(conversionlist) if x == ind ]
# 	y = [naicscodes['name'].unique()[t] for t in x ]
# 	#if maxcol is less than cols then update it
# 	if maxcol < len(y):
# 		maxcol = len(y)
# 	#make shape of y equal to shape of 4 columns
# 	if len(y) != 4:
# 		while len(y) !=4:
# 			y.append('tazo')
# 	#add new naics sectors to company profile
# 	companyprofile.iloc[[t],-4:] = y
# 	companyprofile.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\companyprofiles.csv''')



# from bs4 import BeautifulSoup 
# naics = requests.get('https://www.naics.com/six-digit-naics/')
# print(naics)
# soup = BeautifulSoup(naics.text,'html.parser')
# naicsCode = pd.DataFrame(columns = ['code','name'])
# counter = 0
# temp = []
# row = -1
# for i in soup.find_all('td',{'class':'first_child'}):
# 	print(i.text,'\n')
# 	counter +=1
# 	temp.append(i.text)
# 	if counter % 2 == 0:
# 		row +=1
# 		print(temp)
# 		print(len(temp))
# 		naicsCode.loc[row] = temp
# 		temp = []
# naicsCode.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\naicsCodes.csv''')
# financialStatements = pd.DataFrame()
# counter = 0
# #for loop through all the stock tickers
# for i in stocklist['Ticker']:
# 	financials = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/'+str(i)+'?period=quarter')
# 	data = json.loads(financials.text)
# 	try:
# 		pddata = json_normalize(data['financials'])
# 	except:
# 		continue
# 	pddata['symbol'] = data['symbol']
# 	financialStatements = pd.concat([financialStatements,pddata])
# 	counter += 1
# 	print(counter," ",pddata['symbol'][0])
# financialStatements.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\financials.csv''')
# print(financialStatements.shape)


# Stockprices = pd.DataFrame()
# counter = 0
# #for loop through all the stock tickers
# for i in stocklist['Ticker']:
# 	stockprice = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/'+str(i)+'?serietype=line')
# 	data = json.loads(stockprice.text)
# 	try:
# 		pddata = json_normalize(data['historical'])
# 	except:
# 		continue
# 	pddata['symbol'] = data['symbol']
# 	Stockprices = pd.concat([Stockprices,pddata])
# 	counter += 1
# 	print(counter," ",pddata['symbol'][0])
# Stockprices.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\stockprices.csv''')
# print(financialStatements.shape)
#https://financialmodelingprep.com/api/v3/financial-ratios/AAPL
# financialRatios = pd.DataFrame()
# counter = 0
# #for loop through all the stock tickers
# for i in stocklist['Ticker']:
# 	financialRatio = requests.get('https://financialmodelingprep.com/api/v3/financial-ratios/'+str(i))
# 	data = json.loads(financialRatio.text)
# 	try:
# 		pddata = json_normalize(data['ratios'])
# 	except:
# 		continue
# 	pddata['symbol'] = data['symbol']
# 	financialRatios = pd.concat([financialRatios,pddata])
# 	counter += 1
# 	print(counter," ",pddata['symbol'][0])
# financialRatios.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\financialratios.csv''')
# print(financialRatios.shape)


# companyProfile = pd.DataFrame()
# counter = 0
# #for loop through all the stock tickers
# for i in stocklist['Ticker']:
# 	companyProfiles = requests.get('https://financialmodelingprep.com/api/v3/company/profile/'+str(i))
# 	data = json.loads(companyProfiles.text)
# 	try:
# 		pddata = json_normalize(data['profile'])
# 	except:
# 		continue
# 	pddata['symbol'] = data['symbol']
# 	companyProfile = pd.concat([companyProfile,pddata])
# 	counter += 1
# 	print(counter," ",pddata['symbol'][0])
# companyProfile.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\companyProfile.csv''')
# print(companyProfile.shape)




# finance = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/'+str(stocklist['Ticker'][1])+'?period=quarter')
# data = json.loads(finance.text)
# datat = json_normalize(data['financials'][0])
# datat['symbol'] = data['symbol']
# testmerge = pd.concat([pddata,datat])
# print(testmerge['symbol'])


# print(data['financials'][0]['Gross Margin'])
# #getting stock prices 
# stockprice = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line')
# stock = json.loads(stockprice.text)
# print(stock.keys())
# print(stock['historical'][0])
# txtfile = open('data.txt','ab')
# import pickle
# pickle.dump(stock['historical'][0],txtfile)
# txtfile.close()
# database = open('data.txt','rb')
# print(pickle.load(database).keys())

# I should collect all 
#sector performance
#common commissions
#i will have to calculate sector performance by hand using company profiles and returns
#reconcile the different between stock sectors and naics codes so that the economic data matches

# bea api key  CBD42801-0D63-4A44-B21C-AE2B0006E834

#https://apps.bea.gov/api/data/?&UserID=%20Your-36CharacterKey&method=GetData&DataSetName=GDPbyIndustry&Year=2012,2011&Industry=ALL&tableID=1&Frequency=
#A&ResultFormat=xml
#convert this api into a modular thing function
# def EconData(apikey='CBD42801-0D63-4A44-B21C-AE2B0006E834',headers=None,filename=None,years=None,timeperiod='Q',dataset='GDPbyIndustry',tableid='1',dataformat='json'):
# 	"""
# 	apikey -> bea api key
# 	headers -> the headers need to be the same from the browser
# 	filename -> the output file name
# 	years -> the years to have in a list format
# 	timeperiod -> Q for quarterly A for annual 
# 	dataset -> GdpByIndustry
# 	tableid -> 1,2,3,4 ...etc use 1 
# 	dataformat -> XML JSON CSV


# 	"""
# 	header = {
#  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#  'Accept-Encoding':'gzip, deflate, br',
#  'Accept-Language':'en-US,en;q=0.9',
#  'Cache-Control':'max-age=0',
#  'DNT':'1',
#  'Host':'apps.bea.gov',
#  'Sec-Fetch-Mode':'navigate',
#  'Sec-Fetch-Site':'none',
#  'Sec-Fetch-User':'?1',
#  'Connection':'keep-alive',
#  'Upgrade-Insecure-Requests':'1',
#  'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
#  }
# 	request ='https://apps.bea.gov/api/data/?&UserID='
# 	apikey = apikey
# 	method = '&method=GetData&DataSetName='
# 	dataset = dataset 
# 	years ='&Year='+','.join(years)
# 	timeperiod = timeperiod
# 	tableid = tableid
# 	formatstring = '&ResultFormat='
# 	dataformat = dataformat
# 	industry = '&Industry=ALL&tableID='
# 	freq = '&Frequency='
# 	request = request + apikey + method + dataset + years + industry + tableid + freq + timeperiod + formatstring + dataformat
# 	print(request)
# 	return json_normalize(json.loads(requests.get(request,headers=header).text)['BEAAPI']['Results']['Data']).to_csv(filename)
# print(EconData(years=['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'],filename=r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\gdpbyyear.csv'''))


#sector performance is the sector performance from the sector from the day previously. did it go up yesterday in percentage % or not
#look for all the stocks in the stock market with the same stock sector and then do the math - average of sector price 1 day ago / average of sector price 2 days ago 

#  bea = requests.get(r'''https://apps.bea.gov/api/data/?&UserID=CBD42801-0D63-4A44-B21C-AE2B0006E834&method=GetData&DataSetName=GDPbyIndustry&Year=2012&Industry=ALL&tableID=1&Frequency=Q&ResultFormat=json''',headers={
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'en-US,en;q=0.9',
# 'Cache-Control':'max-age=0',
# 'DNT':'1',
# 'Host':'apps.bea.gov',
# 'Sec-Fetch-Mode':'navigate',
# 'Sec-Fetch-Site':'none',
# 'Sec-Fetch-User':'?1',
# 'Connection':'keep-alive',
# 'Upgrade-Insecure-Requests':'1',
# #'Cookie':'__cfduid=d28c38cb0faa35be42abee7af552258601574197679; _ga=GA1.2.349049895.1574197680; _gid=GA1.2.677132747.1574197680; JSESSIONID=34728954F3850CC69F3FAEA680204422.cfusion; _ga=GA1.3.349049895.1574197680; _gid=GA1.3.677132747.1574197680; _4c_=fVJNj9owFPwrK59x8Fdsh1vVSlUPvW3VI3Jsh0QEHDmG7HbFf%2B8zBNilq3KI8Hhm8mZe3tDU%2Bj1a0VIJRojUXHG%2BQFv%2FOqLVG7JDfh7z4xB7tEJtSsO4Wi6naSpqb4pNOC6bEHdLM26x2WP%2FMviY0ALZ4DzwaVVQWlAA0h84Yk4I%2FB9icAeb1ul1yKTJ10%2Bj28KF88fO%2BvXUudRmdcnlHW19t2kTwFqKjA4xUwpWwmHq9i5Mj8IZvQkVY4DWMUyjz%2BKvbQw7%2F6Q0oAECo99nwQjH6Bsf45n1PvMmhE3vCxt2SyCNXcrzz0XMAHR3wfAFG6A%2BlKfpgzV95kPhC%2FT9y%2FrXj29w4qIiotJVWeQl0EpJnTt6jt1m4%2BNPn9rggPYcjetSF%2Famz%2BFhZ9BLYw59btvldLY349hZ58dtCgM6LdDLvFitiKZKCthCgi1CfyT%2FgBE7N28YOWosYb7CqpIei4YyXJfc4oZISwivmTm3d%2FbUMCaHOTWpwOTYXT0aqSvbGIadqBQW2tXYWOaxdFwzEChfcnSfizABc5Vynovq61hDPzvSO5kyeJ3m7EoWtxDDcWbLd5GFoFySTyJf1o%2F9%2Fj%2By6l8ZlH1NqZT1VnKPiTYcUgqFK1FDZ15boxWnRjj06EnVJ577W%2Fm3Vd76FQRUTACtG9K1jvMXouFGc%2FLABSRzr47m0etyH6eb1XwhmZIfqRk5nU5%2FAQ%3D%3D',
# 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'})
# bea = bea.text
# print(len(bea))
# print(bea[0:100])
# bea = json.loads(bea)
# data = json_normalize(bea['BEAAPI']['Results']['Data'])
# data.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\gdpdata.csv''')
#economic data per sector
#do feature engineering on random features like were earning reports better than last time or not 


stocks = pd.read_csv('stockprices.csv')
lasttenyears = pd.DataFrame()
counter = 0
for i in stocklist['Ticker'].unique():
	print(i)
	print(type(i))
	x = stocks[stocks['symbol'] == i]
	print(type(x))
	print(x.shape)
	tenyears = x[x['date'] > '2009-11-01']
	print(tenyears.shape)
	stocks = pd.concat([lasttenyears,tenyears])
	print(stocks.shape)
	counter += 1
	print(counter)
	if counter > 10:
		break
stocks.to_csv(r'''C:\Users\Michael\Desktop\Accounting-Learning\flatiron\finalproject\lasttenyears.csv''')
#then I should think about already known finance methods
#some common finance day trading/ swing trading methods
#simple strategy sector rotation momentum https://quantpedia.com/strategies/sector-momentum-rotational-system/
#low volatility stocks https://quantpedia.com/strategies/low-volatility-factor-effect-in-stocks-long-only-version/
#pairs trading
#FSCORE or gains points based on amount of positive indicators, buy reversals when it goes from bad to good
#Warren buffets butt stock trick 
#buy all the stocks with the lowest amount of shorts and hold long
#use ben grahams millenial money stock tips https://www.quantopian.com/posts/patrick-oshaughnessys-millennial-money-value-investing-algorithm-number-fundamentals

#sector performance is the sector performance from the sector from the day previously. did it go up yesterday in percentage % or not
#look for all the stocks in the stock market with the same stock sector and then do the math - average of sector price 1 day ago / average of sector price 2 days ago 



#then I could run my own models to see which features are most important such as 
# a random forest tree 

# i could do random forests ensembles of price going up in 1 year price going up 3 years
# etc . random forest price going up 10% etc...
# do PCA dimensionality reduction to see which features are making up the returns
#I could train an lstm cnn combo and see what kind of returns I can get

