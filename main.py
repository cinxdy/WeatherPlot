import urllib.request as r
import json
from datetime import datetime
from matplotlib import pyplot as plt
from toolForDebug import Dprint
debugMode = True

def getNow():
    base_date = datetime.today().strftime("%Y%m%d")
    base_hour = datetime.today().strftime("%H")
    base_minute = datetime.today().strftime("%M")
    if int(base_minute) < 30:
        base_time = int(base_hour)-1
    else:
        base_time = int(base_hour)
    return int(base_date), base_time


def getItems(base_date,base_time):
    Dprint("<\nsetting request condition")

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
    serviceKey = "BmBFV2vhwRaiT9wOTKaBloEKIV6%2F%2B%2BBgKaPtkWk%2B%2F4l%2FmCne4OyNdieucsL0S1SRWAsPcLWxmTjXKjy7NsALFw%3D%3D"

    dataType = "JSON"


    #흥해읍 기준
    nx = 102
    ny = 96

    option = "?serviceKey="+serviceKey
    request = "&dataType="+dataType+"&base_date="+base_date+"&base_time="+base_time+"&nx="+str(nx)+"&ny="+str(ny)
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
            return float(item.get("obsrValue"))
    return None


def setDateTimeList(lastDate, lastTime, N):
    dateTimeList=[]
    date = lastDate
    time = lastTime    
    for i in range(N):
        if time < 10:
            time_str = "0"+ str(time) +"00"
        else:
            time_str = str(time) +"00"
        dateTimeList.append([str(date),time_str])
        time-=1
        if time<0:
            date -= 1
            time = 23
    
    dateTimeList.reverse()
    Dprint("dateTimeList")
    Dprint(dateTimeList)
    return dateTimeList

def storeIntoList(datelist):
    temperList=[]
    humidList=[]

    for date in datelist:
        print("date",date)
        item = getItems(date[0],date[1])

        value = getValue(item, const_temper)
        temperList.append(value)   
        value = getValue(item, const_humid)
        humidList.append(value)   

    return temperList,humidList



# Show a chart

now = getNow()

x = setDateTimeList(now[0],now[1],23)
y1,y2 = storeIntoList(x)

new_x=[]
for item in x:
    new_x.append(item[1][:2])

Dprint("x")
Dprint(x)

Dprint("new_x")
Dprint(new_x)
Dprint("y1")
Dprint(y1)
Dprint("y2")
Dprint(y2)

fig, ax2 = plt.subplots()
ax1 = ax2.twinx()

ax1.plot(new_x, y1, color='g')
ax2.bar(new_x, y2, color='b')

ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature', color='g')
ax2.set_ylabel('Humidity', color='b')
plt.title("Weather for two days ("+x[0][0][5:6]+"/"+x[0][0][7:8]+"~"+x[len(x)-1][0][7:8]+") near HGU")

plt.show()