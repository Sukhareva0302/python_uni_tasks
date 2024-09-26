import DataGenerator as dg
import matplotlib.pyplot as plt

mu0 = [3, 5, 2]
mu1 = [1, 7, 3]
sigma0= [1, 2, 2]
sigma1 = [3, 2, 1]
N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков – длина массива средних

mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y = dg.norm_dataset_N(mu,sigma,N)

# разделяем данные на 2 подвыборки
trainCount = round(0.7*N*2) # не забываем округлить до целого
Xtrain = X[0:trainCount]
Xtest = X[trainCount:N*2+1]
Ytrain = Y[0:trainCount]
Ytest = Y[trainCount:N*2+1]


plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Скатеррограмма') #Название
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="summer")
plt.show()


