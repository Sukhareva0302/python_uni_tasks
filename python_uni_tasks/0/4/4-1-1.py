import pandas as pd
import numpy as np

def f(x):
    print('Индексы')
    print(x.index)
    print('Типы данных')
    print(x.dtypes)
    print('Описательная статистика')
    print(x.describe (include='all'))
    print('Первые 5 строк:')
    print(x.head()) #for N+2 columns you need to print x[['<name1>', '<name2;]].head(),
                    #but since my number is 20 and there is only 17 columns, I simply didn't do it
table = pd.read_csv('diabetes_data_upload.csv')
f(table)
