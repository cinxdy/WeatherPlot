import urllib.request as r
import json
from datetime import datetime

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
serviceKey = "BmBFV2vhwRaiT9wOTKaBloEKIV6%2F%2B%2BBgKaPtkWk%2B%2F4l%2FmCne4OyNdieucsL0S1SRWAsPcLWxmTjXKjy7NsALFw%3D%3D"

dataType = "JSON"

#오늘 날짜 00시 기준
base_date = datetime.today().strftime("%Y%m%d")
base_time = "0000"

#흥해읍 기준
nx = 102
ny = 96

option = "?serviceKey="+serviceKey
request = "&dataType="+dataType+"&base_date="+base_date+"&base_time="+base_time+"&nx="+str(nx)+"&ny="+str(ny)

url_full = url + option + request

responseBody = r.urlopen(url_full).read().decode('utf-8')
jsonArray = json.loads(responseBody) 
print(jsonArray)
#storeInfosArray = jsonArray.get("") 
#print(storeInfosArray)
#print("test end")