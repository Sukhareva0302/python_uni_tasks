import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import DataGenerator as dg
import estimation as es
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.metrics import roc_auc_score

mu0 = [3, 5, 2] #[3, 5, 2]  [1, 7, 3]
mu1 = [1, 7, 3]
sigma0= [1, 2, 2]
sigma1 = [3, 2, 1]
N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков – длина массива средних

mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y, class0, class1 = dg.norm_dataset(mu,sigma,N) #X, Y, class0, class1 = dg.norm_dataset(mu,sigma,N) | X, Y= dg.norm_dataset_N(mu,sigma,N)

# разделяем данные на 2 подвыборки
trainCount = round(0.7*N*2) # не забываем округлить до целого
Xtrain = X[0:trainCount]
Xtest = X[trainCount:N*2+1]
Ytrain = Y[0:trainCount]
Ytest = Y[trainCount:N*2+1]

Nvar = 20
clf = DecisionTreeClassifier(random_state=0, max_depth=12).fit( Xtrain, Ytrain)

Pred_test = clf.predict(Xtest)
Pred_train = clf.predict(Xtrain)
Pred_test_proba = clf.predict_proba(Xtest)

print('DecisionTreeClassifier:')
print(es.EstimateTestAndTrain(Pred_test, Ytest, Pred_train, Ytrain))

skplt.metrics.plot_roc_curve(Ytest, Pred_test_proba, figsize = (10,10))
plt.show()

# Расчет площади под кривой
AUC = roc_auc_score(Ytest, Pred_test_proba[:,1])
print("AUC tree:"+str(AUC))

maxarea=0
treecount=0
for i in range(1, 300, 10):
    clf = RandomForestClassifier(n_estimators=i,random_state=0).fit( Xtrain, Ytrain)
    if maxarea<roc_auc_score(Ytest, clf.predict_proba(Xtest)[:,1]):
        maxarea=roc_auc_score(Ytest, clf.predict_proba(Xtest)[:,1])
        treecount=i

clf = RandomForestClassifier(n_estimators=treecount,random_state=0).fit( Xtrain, Ytrain)
#clf = RandomForestClassifier(random_state=0).fit( Xtrain, Ytrain)
Pred_test = clf.predict(Xtest)
Pred_train = clf.predict(Xtrain)
Pred_test_proba = clf.predict_proba(Xtest)
Pred_trein_proba = clf.predict_proba(Xtest)

print('RandomForestClassifier:')
print(es.EstimateTestAndTrain(Pred_test, Ytest, Pred_train, Ytrain))

skplt.metrics.plot_roc_curve(Ytest, Pred_test_proba, figsize = (10,10))
plt.show()

# Расчет площади под кривой
AUC = roc_auc_score(Ytest, Pred_test_proba[:,1])
print('tree count:', treecount)
print("AUC tree:"+str(AUC))

plt.subplot(1,2,1)
plt.hist(Pred_trein_proba[Ytrain,1], bins='auto', alpha=0.7)
plt.hist(Pred_trein_proba[~Ytrain,1], bins='auto', alpha=0.7)
plt.title('Результат классификации, трейн')
plt.subplot(1,2,2)
plt.hist(Pred_test_proba[Ytest,1], bins='auto', alpha=0.7)
plt.hist(Pred_test_proba[~Ytest,1], bins='auto', alpha=0.7) # т.к массив с вероятностями имеет два столбца, мы берем один - первый
plt.title("Результаты классификации, тест")
plt.show()


