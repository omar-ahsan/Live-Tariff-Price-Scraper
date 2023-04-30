import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def procedure(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')
    json_str = soup.p.text
    data = json.loads(json_str)

    tariff_usage = [d['TariffUsage'] for d in data]
    return tariff_usage


year = input('Year : ')
month = input('Month : ')
day = input('Day : ')
date1 = year + '-' + month + '-' + day
end_day = int(day) + 1
date2 = year + '-' + month + '-' + str(end_day)

url = f"https://mijn.easyenergy.com/nl/api/tariff/getapxtariffs?startTimestamp={date1}T19:00:00.000Z&endTimestamp={date2}T19:00:00.000Z&grouping=&includeVat=true"
results = procedure(url)
timestamps = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
              '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
              '22:00', '23:00']

df = pd.DataFrame({'Time': timestamps, 'Price': results})
df.to_excel(r'results.xlsx', index=False)
