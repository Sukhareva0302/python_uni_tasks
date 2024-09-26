import pandas as pd
import numpy as np
from sklearn import preprocessing

table = pd.read_csv('diabetes_data_upload.csv')
print("Изначальная таблица")
print(table)
print("")

Y=table.iloc[:,16].values
print("Таблица выходных значений")
print(Y)
print("")

X=table.drop(['class'], axis=1).values
Xs=X[:,0]
Xs=preprocessing.scale(Xs)
for i in range(0,len(Xs)):
               X[i,0]=Xs[i]
print("Таблица входных значений")
print(X)
print("")


enc = preprocessing.OneHotEncoder()
enc.fit(X)
preprocessing.OneHotEncoder()
X=enc.transform(X).toarray()

print("Таблица входных значений после преобразования")
print(X)
print("")

df = pd.DataFrame(X)
df.to_csv("X.csv")
df = pd.DataFrame(Y)
df.to_csv("Y.csv")

print("Таблицы входных и выходных значений были сохранены в .csv файлы X и Y соответственно")

