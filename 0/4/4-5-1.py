import pandas as pd
import numpy as np

table = pd.read_csv('diabetes_data_upload.csv')

print(pd.isna(table))
table.dropna(how='any')
print(table)

