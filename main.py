import urllib.request as r
import json
from datetime import datetime
from matplotlib import pyplot as plt

debugMode = True




def getItems(base_date):
    Dprint("<\nsetting request condition")

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
    serviceKey = "BmBFV2vhwRaiT9wOTKaBloEKIV6%2F%2B%2BBgKaPtkWk%2B%2F4l%2FmCne4OyNdieucsL0S1SRWAsPcLWxmTjXKjy7NsALFw%3D%3D"

    dataType = "JSON"

    #오늘 날짜 06시 기준
    #base_date = datetime.today().strftime("%Y%m%d")
    #base_date = "20200812"
    base_time = "0600"

    #흥해읍 기준
    nx = 102
    ny = 96

    option = "?serviceKey="+serviceKey
    request = "&dataType="+dataType+"&base_date="+str(base_date)+"&base_time="+base_time+"&nx="+str(nx)+"&ny="+str(ny)
    url_full = url + option + request

    Dprint(">")
    Dprint("<\nopen URL")

    response = r.urlopen(url_full).read().decode('utf-8')
    Dprint(">")
    
    jsonArray = json.loads(response) 
    Dprint(jsonArray)
    items =jsonArray.get("response").get("body").get("items").get("item") 
    Dprint("items>")
    Dprint(items)

    return items

const_temper = "T1H"
const_humid = "REH"

def getValue(items,category):
    for item in items:
        if item.get("category")==category:
            return item.get("obsrValue")
    return None


def setDateList(lastDate, N):
    dateList=[]
    date = lastDate    
    for i in range(N):
        dateList.append(date)
        date-=1
    dateList.reverse()
    Dprint("dateList")
    Dprint(dateList)
    return dateList

def storeIntoList(datelist):
    temperList=[]
    humidList=[]

    for date in datelist:
        print("date",date)
        item = getItems(date)

        value = getValue(item, const_temper)
        temperList.append(value)   
        value = getValue(item, const_humid)
        humidList.append(value)   

    return temperList,humidList




Dprint("test start")
date = 20200811
storeInfosArray = getItems(date)
Dprint("items")
Dprint(storeInfosArray)
Dprint("test temper")
Dprint(getValue(storeInfosArray,const_temper))
Dprint("test humid")
Dprint(getValue(storeInfosArray,const_humid))
Dprint("test end")




# Show a chart
today = 20200812
x = setDateList(today,2)
y1,y2 = storeIntoList(x)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature', color='g')
ax2.set_ylabel('Humidity', color='b')

plt.show()