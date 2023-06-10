import csv
from datetime import datetime
from pprint import pprint



with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("==========")
        YEAR_DATE= datetime.strptime(laureate["year"],"%Y")
        BORN_DATE=datetime.strptime(laureate["born"],"%Y-%m-%d")
        print("age",YEAR_DATE.year-BORN_DATE.year)
        break
