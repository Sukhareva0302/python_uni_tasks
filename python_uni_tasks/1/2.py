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
X, Y, class0, class1 = dg.norm_dataset(mu,sigma,N)

# разделяем данные на 2 подвыборки
trainCount = round(0.7*N*2) # не забываем округлить до целого
Xtrain = X[0:trainCount]
Xtest = X[trainCount:N*2+1]
Ytrain = Y[0:trainCount]
Ytest = Y[trainCount:N*2+1]


# построение гистограмм распределения для всех признаков
for i in range(0, col):
    _ = plt.hist(class0[:, i], bins='auto', alpha=0.7) #параметр alpha позволяет задатьпрозрачность цвета
    _ = plt.hist(class1[:, i], bins='auto', alpha=0.7)
    plt.xlabel('Ось х') #Подпись для оси х
    plt.ylabel('Ось y') #Подпись для оси y
    plt.title("Гистограмма №{}".format(i+1))
    plt.savefig('hist_'+str(i+1)+'.png')# сохранение изображения в файл
    plt.show()
# построение одной скатеррограммы по выбранным признакам
plt.scatter(class0[:,0], class0[:,2], marker=".", alpha=0.7)
plt.scatter(class1[:,0], class1[:,2], marker=".", alpha=0.7)
plt.savefig('scatter_'+str(i+1)+'.png')
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Скатеррограмма') #Название
plt.show()

