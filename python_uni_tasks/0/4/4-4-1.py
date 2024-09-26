import pandas as pd
import numpy as np

table = pd.read_csv('diabetes_data_upload.csv')

tableNew=table.sort_values(by='Obesity') #since there is no 21 colunm, I choose 15 and 16
print('Key 1= 16 column "Obesity"')
print(tableNew)
tableNew=table.sort_values(by='class')
print('Key 2= 17 column "class"')
print(tableNew)
tableNew=table.sort_values(by='Age')
print('Key 3= "Age"')
print(tableNew)

