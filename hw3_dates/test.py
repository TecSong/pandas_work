### TEST FUNCTION: test_api_call
# DO NOT REMOVE THE LINE ABOVE

import pandas as pd
import requests
import json

url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

params = {"$where": ("created_date>='2020-03-01T00:00:00' AND created_date<='2020-03-31T11:59:59'"
                     "AND closed_date>='2020-03-01T00:00:00' AND closed_date<='2020-03-31T11:59:59'"
                     "AND (incident_zip = '10025' OR incident_zip = '10026' OR incident_zip = '10027')"),
          "$select": ("unique_key,created_date,closed_date,agency_name,"
                      "complaint_type,descriptor,incident_zip,resolution_description,"
                      "Latitude,Longitude"),
          "$limit": 5000}

resp = requests.get(url, params=params)
if resp.status_code != 200:
   print("Non-200 status:", resp.text)

data = resp.content
py_data = json.loads(data)
df = pd.DataFrame(py_data)

# task2
import numpy as np

busy_zip = df.loc[:, 'incident_zip'].value_counts().idxmax()

filter_mask = df['created_date']==df['closed_date']
perc_instant = float(len(df[filter_mask])) / float(len(df))

nan_df = df[df['closed_date'].isnull()]
perc_open = float(len(nan_df)) / float(len(df))

popular_complaint = df.loc[:, 'complaint_type'].value_counts().idxmax()

# task3 --todo