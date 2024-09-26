import pandas as pd
import numpy as np
import time

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
table.to_csv("output1.csv")

import csv
start=time.time()
with open('output1.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print (data)
sum_num_F=0
sum_num_M=0
len_M=0
len_F=0
for i in range(1,len(data)):
    gender=data[i][2]
    if gender == '1':
        sum_num_M=sum_num_M+int(data[i][1])
        len_M=len_M+1
    else:
        sum_num_F=sum_num_F+int(data[i][1])
        len_F=len_F+1

avg_F=sum_num_F/len_F
avg_M=sum_num_M/len_M
print("Средний врзраст мужчин =", avg_M)
print("Средний врзраст женщин =", avg_F)
end=time.time()
print('Time=', end-start)
start=time.time()
data = pd.read_csv('output1.csv')
print('Averege age by:', data.groupby('1')['0'].mean())
end=time.time()
print('Time=', end-start)

