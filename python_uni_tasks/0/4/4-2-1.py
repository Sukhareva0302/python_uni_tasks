import pandas as pd
import numpy as np

table = pd.read_csv('diabetes_data_upload.csv')

TableYes=table[table['Obesity']=='Yes'] #since there is no 21 colunm, I choose 15
TableNo=table[table['Obesity']=='No']
print('Only Yes')
print(TableYes)
print('Only No')
print(TableNo)
