import pandas as pd
import numpy as np

def f(x, a):
    if x == a:
        return '1'
    else:
        return '0'

table = pd.read_csv('diabetes_data_upload.csv')
print('Before:')
print(table.dtypes)
print(table)
table['Gender']=table['Gender'].apply(lambda x: f(x, 'Male'))
table['Polyuria']=table['Polyuria'].apply(lambda x: f(x, 'Yes'))
table['Polydipsia']=table['Polydipsia'].apply(lambda x: f(x, 'Yes'))
table['sudden weight loss']=table['sudden weight loss'].apply(lambda x: f(x, 'Yes'))
table['weakness']=table['weakness'].apply(lambda x: f(x, 'Yes'))
table['Polyphagia']=table['Polyphagia'].apply(lambda x: f(x, 'Yes'))
table['Genital thrush']=table['Genital thrush'].apply(lambda x: f(x, 'Yes'))
table['visual blurring']=table['visual blurring'].apply(lambda x: f(x, 'Yes'))
table['Itching']=table['Itching'].apply(lambda x: f(x, 'Yes'))
table['Irritability']=table['Irritability'].apply(lambda x: f(x, 'Yes'))
table['Itching']=table['Itching'].apply(lambda x: f(x, 'Yes'))
table['delayed healing']=table['delayed healing'].apply(lambda x: f(x, 'Yes'))
table['partial paresis']=table['partial paresis'].apply(lambda x: f(x, 'Yes'))
table['muscle stiffness']=table['muscle stiffness'].apply(lambda x: f(x, 'Yes'))
table['Alopecia']=table['Alopecia'].apply(lambda x: f(x, 'Yes'))
table['Obesity']=table['Obesity'].apply(lambda x: f(x, 'Yes'))
table['class']=table['class'].apply(lambda x: f(x, 'Positive'))
table.columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15', '16']
table=table.astype(int)
print('After:')
print(table.dtypes)
print(table)
