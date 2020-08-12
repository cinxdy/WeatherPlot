
import urllib.request as r
import json
from datetime import datetime
from matplotlib import pyplot as plt

from toolForDebug import Dprint


def getItems():
    
    Dprint("<\nsetting request condition")

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
    serviceKey = "BmBFV2vhwRaiT9wOTKaBloEKIV6%2F%2B%2BBgKaPtkWk%2B%2F4l%2FmCne4OyNdieucsL0S1SRWAsPcLWxmTjXKjy7NsALFw%3D%3D"

    dataType = "JSON"

    base_date = datetime.today().strftime("%Y%m%d")
    base_time = datetime.today().strftime("%H")+"00"

    #흥해읍 기준
    nx = 102
    ny = 96

    option = "?serviceKey="+serviceKey
    request = "&dataType="+dataType+"&base_date="+str(base_date)+"&base_time="+base_time+"&nx="+str(nx)+"&ny="+str(ny)
    url_full = url + option + request
    print(url_full)

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


print(getItems())