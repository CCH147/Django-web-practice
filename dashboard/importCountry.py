import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append("/django chart/C111112133")
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','datavisual.settings')
import django
django.setup()

from dashboard.models import CountryData

CountryData.objects.all().delete()

unit = CountryData()

url = 'https://www.worldometers.info/world-population/population-by-country/'

r = requests.get(url)

soup = BeautifulSoup(r.content)

countries = soup.find_all("table")[0]
df = pd.read_html(str(countries))[0]

def function(a,b):
    
    data = pd.DataFrame(
        {'a': df[a],
         'b': df[b]
        
        })
    return data
i=10000000
df = function('Country (or dependency)','Population (2020)')

df.columns=['country','population']
df['population'] = df['population'] / i
df['population'] = df['population'].astype(int)

df_filter = df.copy()
df_data = df_filter.iloc[0:10]
for item in range(0,10):
        new_rec = CountryData(country = df_data.iat[item,0],
                  population = df_data.iat[item,1])
        new_rec.save()
        
"""""
unit.country = df_data['country']
unit.population = df_data['population'].values


"""""

print(df_data.iat[0,1])
print(df_data.columns)



