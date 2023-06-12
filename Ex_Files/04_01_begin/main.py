import requests
import json
from pprint import pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

#with open("bank.json", "w") as f:
#    json.dump(last_twenty_years, f, indent=2)

pprint(last_twenty_years) 

#for year in last_twenty_years:
#    display_width = year["value"] // 10_000_000
#    print(year["date"], "=" * display_width)

for year in last_twenty_years:
    if year["value"] is not None:
        display_width = year["value"] // 10_000_000
        print(f'{year["date"]}: {year["value"]}', "=" * display_width)
