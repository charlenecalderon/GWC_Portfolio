import pandas
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

#print(data)
data.EDT
#print(data.EDT)
data.EDT.head()
print(data.EDT.head()
