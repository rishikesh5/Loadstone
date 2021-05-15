# -*- coding: utf-8 -*-
#use this link to access the Colab notebook : https://colab.research.google.com/drive/186PY1nIjIyZ1IU7LB7Cu0xx9qxJRqKtu?usp=sharing
import pandas as pd

grill_details = pd.read_csv('SheetA.csv')
grill_details

usr_exp = pd.read_csv('SheetB.csv')
 usr_exp

usr_pref = pd.read_csv('SheetC.csv')
usr_pref

#checking for missing values
grill_details.isnull().sum()

#unique values 
usr_pref.value_counts()
usr_exp.value_counts()

#no missing values found
usr_pref.isnull().sum()
usr_exp.isnull().sum()

#Q2.Which grill type is more fuel efficient based on sheetA
grill_details
#Propane grill type is more fuel efficient based on sheetA

#Q3. Which grill type has more market share
#According to sheet A Propane grill type has more market share

#Q4. Based on the cookoff data which grill type cost more fuel on a long
#Charcoal Costs more fuel in the long run

#Q9 Json to csv

from pandas.io.json import json_normalize

with open('SheetC.json') as f:
  d = json.loads(f.read())

json_data = json.loads(d[0].get('test_result'))
parsed_data = list()

for i in range(1, len(json_data)):
  flat_json = dict()
  current_row = json_data.get(str(i))
  row_metadata = current_row.get('meta_data')
  for x in row_metadata:
    flat_json[x] = row_metadata[x]
  flat_json['sample_item_index'] = current_row['sample_item_index']
  survey_result = current_row.get('survey_result')
  for x in survey_result:
    flat_json[x] = survey_result[x]
  parsed_data.append(flat_json)
df = pd.DataFrame(parsed_data)
df.head()

df.to_csv('Json_to_csv.csv', index_label='P.key')





