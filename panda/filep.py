import pandas
from datetime import datetime
import matplotlib.pyplot as plt
data = pandas.read_csv("weather_year.csv")
#print(data)

#print(len(data))
data.columns
#print(data.columns)
data["EDT"]
#print(data.EDT.head(20))
data.columns= ['EDT', 'maxTemp', 'meanTemp', 'minTemp',
       'maxDew', 'meanDew', 'minDew', 'maxHum',
       'meanHum', 'minHum', 'maxSeaLevel',
       'meanSeaLevel', 'minSeaLevel',
       'maxVis', 'meanVis', 'minVis',
       'maxWind', 'meanWind', 'maxGust',
       'precip', 'cloudCover', 'events', 'windDir']

###print(data)
##data.EDT
###print(data.EDT)
##data.EDT.head()
###print(data.EDT.head(10))
##data.meanTemp.head()
###print(data.meanTemp.head())
##data.meanTemp.std()
###print(data.meanTemp.std())
##data.std()
###print(data.std())
##data.EDT.head()
###print(data.EDT.head())
##first_EDT = data.EDT.values[0]
###print(first_EDT)
##
##FD= datetime.strptime(first_EDT, "%Y-%m-%d")
##print(FD)
##data.EDT = data.EDT.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
##data.EDT.head()
##print(data.EDT.head())
##data.index = data.EDT
##print(data.index)
###data.ix[datetime(2012,8, 19)]
###print(data.ix[datetime(2012,8, 19)])
##data = data.drop(["EDT"], axis=1)
##data.columns
###print(data.columns)
##empty = data.apply(lambda col: pandas.isnull(col))
###print(empty)
##empty.events.head(10)
###print(empty.events.head)
##data.dropna(subset=["events"])
###print(data.dropna)
##data.events = data.events.fillna("")
##data.events.head(10)
##print(data.events)
##data.irow(0)
##print(data.irow)

plt.xlabel("Day")
plt.ylabel("wind")
plt.title("Day vs Temp")


plt.plot(data.maxWind, color="purple")
plt.plot(data.meanWind, color="pink")
plt.grid(True)
plt.show()



