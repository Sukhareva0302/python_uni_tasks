import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


df = pd.read_csv('X.csv')
X= df.drop(df.columns [0], axis=1).values
df = pd.read_csv('Y.csv')
Y= df.drop(df.columns [0], axis=1).values
print('Изначальные входные и выходные значения:')
print(X)
print()
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 20)
print('Размер обучающей выборки входных и выходных значений:')
print(X_train.shape)
print(Y_train.shape)
print()
print('Размер тестовой выборки входных и выходных значений:')
print(X_test.shape)
print(Y_test.shape)
print()


model = LogisticRegression(random_state=20).fit(X_train,np.ravel(Y_train))
Y_pred = model.predict(X_test)
print('Оценка качества показаний (где идеальный результат =1)')
print(accuracy_score(Y_test, Y_pred))
print(f1_score(Y_test, Y_pred, average=None))

param_range = [100, 10, 1, 0.1, 0.01, 0.001]
for i in range(0, len(param_range)):
    model = LogisticRegression(C=param_range[i],random_state=20).fit(X_train,np.ravel(Y_train))
    Y_pred = model.predict(X_test)
    print('Оценка качества показаний (где идеальный результат =1) для С=',param_range[i])
    print(accuracy_score(Y_test, Y_pred))
    print(f1_score(Y_test, Y_pred, average=None))
