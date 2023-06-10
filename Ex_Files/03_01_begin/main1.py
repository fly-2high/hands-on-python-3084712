import csv

from pprint import pprint

with open("laureates.csv","r") as f:
    READER = csv.DictReader(f)
    LAUREATES= list(READER)

for LAUREATE in LAUREATES:
    if LAUREATE["surname"]=="Einstein":
        pprint(LAUREATE)
        break



