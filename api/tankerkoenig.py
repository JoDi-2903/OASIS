import json
import requests
import pandas as pd

url = 

response = requests.get(url).json()
df = pd.DataFrame.from_dict(response.get('stations'))

dfLowestPrice = df.index[0]
print(df)
for i in df.index:
    if(df['price'][i] < dfLowestPrice):
        dfLowestPrice['price'] = df['price'][i]

print(dfLowestPrice)