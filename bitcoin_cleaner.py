import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
dataSourcePath = 'F:\\cursos\\tipologia\\crypto\\coin_data.csv'
datasource = pd.read_csv(dataSourcePath)
print('Cleaning Data')
numberOfZeros = datasource['Currency'].isnull().sum()
if numberOfZeros > 0:
	rowFilter= datasource['Currency'].notnull()
	tempDataSource= datasource[rowFilter].copy()
	datasource= tempDatasource
	print('Rows with zero values were removed')
else:
	print ("Column Currency not contains null values")

numberOfZeros = (datasource['Low'] == 0).sum()
if numberOfZeros > 0:
	rowFilter=datasource['Low'] > 0
	tempDataSource= datasource[rowFilter].copy()
	datasource= tempDatasource
	print('Rows with zero values in column Low were removed')
else:
	print ("Column Low not contains zeros")	

numberOfZeros = (datasource['High'] == 0).sum()
if numberOfZeros > 0:
	rowFilter=datasource['Low'] > 0
	tempDataSource= datasource[rowFilter].copy()
	datasource= tempDatasource
	print('Rows with zero values in column High were removed')
else:
	print ("Column High not contains zeros")
weekDayConvert= lambda x: days[datetime.strptime(x,"%b %d, %Y").date().weekday()]
dayConvert= lambda x: datetime.strptime(x,"%b %d, %Y").date()
removeComma= lambda x: x.replace(',','')
removeOther= lambda x: x.replace('-','0')
convert2MM= lambda x: x / 1000000
datasource['Market Cap'] = datasource['Market Cap'].apply(removeComma)
datasource['Market Cap'] = datasource['Market Cap'].apply(removeOther)
datasource['MarketCap'] =  pd.to_numeric(datasource['Market Cap'])
datasource['MarketCap'] =  datasource['MarketCap'].apply(convert2MM)
datasource['Diff'] = datasource['High'] - datasource['Low']
datasource['NewDate'] = datasource['Date'].apply(dayConvert)
datasource['WeekDay']= datasource['Date'].apply(weekDayConvert)
datasource['NewDate'] = pd.to_datetime(datasource['NewDate'])
datasource.info()
datasource.dtypes
rowFilter=datasource['NewDate'] >= '2017-01-01 00:00:00'
tempDataSource= datasource[rowFilter].copy()
top5MarketCap=tempDataSource.groupby(['Currency'], sort=False)['MarketCap'].max().sort_values(ascending=False).head(5)
top5MarketCap.plot(kind='barh',rot=0)
#plt.show()
rowFilter=tempDataSource['Currency'] == 'bitcoin'
bitcoinDS= tempDataSource[rowFilter].copy()
del bitcoinDS['Market Cap']
del bitcoinDS['High']
del bitcoinDS['Low']
del bitcoinDS['Date']
del bitcoinDS['Open']
del bitcoinDS['Close']
del bitcoinDS['Volume']
del bitcoinDS['Currency']
#Usefull to know the datè
#del bitcoinDS['NewDate']
groups = bitcoinDS.groupby("WeekDay").groups
groupSunday=bitcoinDS.groupby("WeekDay").get_group("Sunday")["Diff"].tolist()
groupMonday=bitcoinDS.groupby("WeekDay").get_group("Monday")["Diff"].tolist()
groupTuesday=bitcoinDS.groupby("WeekDay").get_group("Tuesday")["Diff"].tolist()
groupWednesday=bitcoinDS.groupby("WeekDay").get_group("Wednesday")["Diff"].tolist()
groupThursday=bitcoinDS.groupby("WeekDay").get_group("Thursday")["Diff"].tolist()
groupFriday=bitcoinDS.groupby("WeekDay").get_group("Friday")["Diff"].tolist()
groupSaturday=bitcoinDS.groupby("WeekDay").get_group("Saturday")["Diff"].tolist()
f_val, p_val = stats.f_oneway(groupSunday, groupMonday, groupTuesday, groupWednesday, groupThursday,groupFriday,groupSaturday)
print("Bitcoin ANOVA One-Way P Value is:" ,p_val)
bitcoinDSDay=bitcoinDS.groupby(['WeekDay'], sort=False)['Diff'].mean().sort_values(ascending=False)
bitcoinDSDay.plot(kind='barh',rot=0)
plt.show()
#Ethereum
rowFilter=tempDataSource['Currency'] == 'ethereum'
ethereumDS= tempDataSource[rowFilter].copy()
del ethereumDS['Market Cap']
del ethereumDS['High']
del ethereumDS['Low']
del ethereumDS['Date']
del ethereumDS['Open']
del ethereumDS['Close']
del ethereumDS['Volume']
del ethereumDS['Currency']
groupSunday=ethereumDS.groupby("WeekDay").get_group("Sunday")["Diff"].tolist()
groupMonday=ethereumDS.groupby("WeekDay").get_group("Monday")["Diff"].tolist()
groupTuesday=ethereumDS.groupby("WeekDay").get_group("Tuesday")["Diff"].tolist()
groupWednesday=ethereumDS.groupby("WeekDay").get_group("Wednesday")["Diff"].tolist()
groupThursday=ethereumDS.groupby("WeekDay").get_group("Thursday")["Diff"].tolist()
groupFriday=ethereumDS.groupby("WeekDay").get_group("Friday")["Diff"].tolist()
groupSaturday=ethereumDS.groupby("WeekDay").get_group("Saturday")["Diff"].tolist()
f_val, p_val = stats.f_oneway(groupSunday, groupMonday, groupTuesday, groupWednesday, groupThursday,groupFriday,groupSaturday)
print("Ethereum ANOVA One-Way P Value is:" ,p_val)
ethereumDS=bitcoinDS.groupby(['WeekDay'], sort=False)['Diff'].mean().sort_values(ascending=False)
ethereumDS.plot(kind='barh',rot=0)
plt.show()

#bitcoin-cash
rowFilter=tempDataSource['Currency'] == 'bitcoin-cash'
bitcoincashDS= tempDataSource[rowFilter].copy()
del bitcoincashDS['Market Cap']
del bitcoincashDS['High']
del bitcoincashDS['Low']
del bitcoincashDS['Date']
del bitcoincashDS['Open']
del bitcoincashDS['Close']
del bitcoincashDS['Volume']
del bitcoincashDS['Currency']
groupSunday=bitcoincashDS.groupby("WeekDay").get_group("Sunday")["Diff"].tolist()
groupMonday=bitcoincashDS.groupby("WeekDay").get_group("Monday")["Diff"].tolist()
groupTuesday=bitcoincashDS.groupby("WeekDay").get_group("Tuesday")["Diff"].tolist()
groupWednesday=bitcoincashDS.groupby("WeekDay").get_group("Wednesday")["Diff"].tolist()
groupThursday=bitcoincashDS.groupby("WeekDay").get_group("Thursday")["Diff"].tolist()
groupFriday=bitcoincashDS.groupby("WeekDay").get_group("Friday")["Diff"].tolist()
groupSaturday=bitcoincashDS.groupby("WeekDay").get_group("Saturday")["Diff"].tolist()
f_val, p_val = stats.f_oneway(groupSunday, groupMonday, groupTuesday, groupWednesday, groupThursday,groupFriday,groupSaturday)
print("Bitcoin-cash ANOVA One-Way P Value is:" ,p_val)
bitcoincashDSDay=bitcoincashDS.groupby(['WeekDay'], sort=False)['Diff'].mean().sort_values(ascending=False)
bitcoincashDSDay.plot(kind='barh',rot=0)
plt.show()

#ripple
rowFilter=tempDataSource['Currency'] == 'ripple'
rippleDS= tempDataSource[rowFilter].copy()
del rippleDS['Market Cap']
del rippleDS['High']
del rippleDS['Low']
del rippleDS['Date']
del rippleDS['Open']
del rippleDS['Close']
del rippleDS['Volume']
del rippleDS['Currency']
groupSunday=rippleDS.groupby("WeekDay").get_group("Sunday")["Diff"].tolist()
groupMonday=rippleDS.groupby("WeekDay").get_group("Monday")["Diff"].tolist()
groupTuesday=rippleDS.groupby("WeekDay").get_group("Tuesday")["Diff"].tolist()
groupWednesday=rippleDS.groupby("WeekDay").get_group("Wednesday")["Diff"].tolist()
groupThursday=rippleDS.groupby("WeekDay").get_group("Thursday")["Diff"].tolist()
groupFriday=rippleDS.groupby("WeekDay").get_group("Friday")["Diff"].tolist()
groupSaturday=rippleDS.groupby("WeekDay").get_group("Saturday")["Diff"].tolist()
f_val, p_val = stats.f_oneway(groupSunday, groupMonday, groupTuesday, groupWednesday, groupThursday,groupFriday,groupSaturday)
print("Ripple ANOVA One-Way P Value is:" ,p_val)
rippleDSDay=rippleDS.groupby(['WeekDay'], sort=False)['Diff'].mean().sort_values(ascending=False)
rippleDSDay.plot(kind='barh',rot=0)
plt.show()

#litecoin
rowFilter=tempDataSource['Currency'] == 'litecoin'
litecoinDS= tempDataSource[rowFilter].copy()
del litecoinDS['Market Cap']
del litecoinDS['High']
del litecoinDS['Low']
del litecoinDS['Date']
del litecoinDS['Open']
del litecoinDS['Close']
del litecoinDS['Volume']
del litecoinDS['Currency']
groupSunday=litecoinDS.groupby("WeekDay").get_group("Sunday")["Diff"].tolist()
groupMonday=litecoinDS.groupby("WeekDay").get_group("Monday")["Diff"].tolist()
groupTuesday=litecoinDS.groupby("WeekDay").get_group("Tuesday")["Diff"].tolist()
groupWednesday=litecoinDS.groupby("WeekDay").get_group("Wednesday")["Diff"].tolist()
groupThursday=litecoinDS.groupby("WeekDay").get_group("Thursday")["Diff"].tolist()
groupFriday=litecoinDS.groupby("WeekDay").get_group("Friday")["Diff"].tolist()
groupSaturday=litecoinDS.groupby("WeekDay").get_group("Saturday")["Diff"].tolist()
f_val, p_val = stats.f_oneway(groupSunday, groupMonday, groupTuesday, groupWednesday, groupThursday,groupFriday,groupSaturday)
print("Litecoin ANOVA One-Way P Value is:" ,p_val)
litecoinDSDay=litecoinDS.groupby(['WeekDay'], sort=False)['Diff'].mean().sort_values(ascending=False)
litecoinDSDay.plot(kind='barh',rot=0)
plt.show()


