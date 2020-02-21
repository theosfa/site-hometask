import requests
import json

url = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=921701'

r = requests.get(url)


for i in r.json()["schedules"]:
    if i["weekDay"] == "Пятница":
        for j in i["schedule"]:
            for n in j["weekNumber"]:
                print(n)
