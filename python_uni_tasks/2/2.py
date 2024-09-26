import numpy as np
from sklearn.linear_model import LogisticRegression
import DataGenerator as dg
import estimation as es
import matplotlib.pyplot as plt

mu0 = [1, 7, 3]
mu1 = [1, 7, 3]
sigma0= [1, 2, 2]
sigma1 = [3, 2, 1]
N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков – длина массива средних

mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y, class0, class1 = dg.norm_dataset(mu,sigma,N)

# разделяем данные на 2 подвыборки
trainCount = round(0.7*N*2) # не забываем округлить до целого
Xtrain = X[0:trainCount]
Xtest = X[trainCount:N*2+1]
Ytrain = Y[0:trainCount]
Ytest = Y[trainCount:N*2+1]

Nvar = 20
clf = LogisticRegression(random_state=Nvar,solver='saga').fit( Xtrain, Ytrain)

Pred_test = clf.predict(Xtest)
Pred_test_proba = clf.predict_proba(Xtest)

acc_train = clf.score(Xtrain, Ytrain)
acc_test = clf.score(Xtest, Ytest)

#acc_test = sum(Pred_test==Ytest)/len(Ytest) #подсчет точности вручную
Pred_test_proba1 = clf.predict_proba(Xtrain)
Pred_train = clf.predict(Xtrain)

plt.subplot(1,2,1)
plt.hist(Pred_test_proba1[Ytrain,1], bins='auto', alpha=0.7)
plt.hist(Pred_test_proba1[~Ytrain,1], bins='auto', alpha=0.7)
plt.title('Результат классификации, трейн')
plt.subplot(1,2,2)
plt.hist(Pred_test_proba[Ytest,1], bins='auto', alpha=0.7)
plt.hist(Pred_test_proba[~Ytest,1], bins='auto', alpha=0.7) # т.к массив с вероятностями имеет два столбца, мы берем один - первый
plt.title("Результаты классификации, тест")
plt.show()

TPtest=es.TP(Pred_test, Ytest)
FNtest=es.FN(Pred_test, Ytest)
FPtest=es.FP(Pred_test, Ytest)
TNtest=es.TN(Pred_test, Ytest)
TPtrain=es.TP(Pred_train, Ytrain)
FNtrain=es.FN(Pred_train, Ytrain)
FPtrain=es.FP(Pred_train, Ytrain)
TNtrain=es.TN(Pred_train, Ytrain)

#точность
accuracy_test = sum(Pred_test==Ytest)/len(Ytest)*100
accuracy_train = sum(Pred_train==Ytrain)/len(Ytrain)*100
#precision_test=TPtest/(TPtest + FPtest)
#precision_train=TPtrain/(TPtrain + FPtrain)

#чувствительность
sensitivity_test=TPtest/(TPtest + FNtest)*100
sensitivity_train=TPtrain/(TPtrain + FNtrain)*100

#специфичность
specificity_test=TNtest/(TNtest+FPtest)*100
specificity_train=TNtrain/(TNtrain+FPtrain)*100

import pandas as pd
df = pd.DataFrame([['Train', len(Ytrain),accuracy_train
                    ,sensitivity_train,specificity_train],
                   ['Test', len(Ytest), accuracy_test,
                    sensitivity_test, specificity_test]],
                  columns=[' ', 'Число объектов', 'Точность, %',
                           'Чувствительность, %', 'Специфичность, %'])

#print('Точность, чувствительность и специфичность для тестовой выбоки:')
#print(accuracy_test,'%,',sensitivity_test,'%,', specificity_test,'%')
#print('Точность, чувствительность и специфичность для тренировочной выбоки:')
#print(accuracy_train,'%,',sensitivity_train,'%,', specificity_train,'%')

print(df)
