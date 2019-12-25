import requests
import json

url = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=921701'

r = requests.get(url)

# print(r.json())

weekNumber = 2
subGroup = 1

for i in r.json()["schedules"]:
    if i["weekDay"] == "Среда":
        for j in i["schedule"]:
            for n in j["weekNumber"]:
                if n == weekNumber:
                    if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                        print(j["subject"])
