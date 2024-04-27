import requests
from datetime import datetime
import pandas as pd

def getEmailActivity():
    # Get today's date
    today = datetime.now()
    start_of_day = '%27' + today.replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ') + '%27'
    end_of_day = '%27' + today.replace(hour=23, minute=59, second=59, microsecond=999999).strftime('%Y-%m-%dT%H:%M:%SZ') + '%27'
    url = 'https://digitalstoregames.pythonanywhere.com/email_not_delivery?startdate=' + start_of_day + '&enddate=' + end_of_day
   
    headers = {
        'authorization': 'Bearer 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'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def processJson(json_data):
    df = pd.DataFrame(json_data)
    df = df.where(pd.notna(df), None)
    return df    
        
json_data = getEmailActivity()
df = processJson(json_data)
print(df)
#df.to_csv('output.csv', index=False)

