import pandas as pd
import numpy as np

table = pd.read_csv('diabetes_data_upload.csv')
print(table.dtypes)
table.dtypes.to_csv("output.csv")
