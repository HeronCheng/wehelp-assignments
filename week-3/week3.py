import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
list=data["result"]["results"]
with open("data.csv",mode="w",encoding="utf-8") as file:
    for i in list:
        j=i["file"].split("https://")
        file.write(i["stitle"]+","+i["address"][4:8]+","+i["longitude"]+","+i["latitude"]+","+"https://"+j[1]+"\n")
