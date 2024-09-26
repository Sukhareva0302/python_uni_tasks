import numpy as np
import matplotlib.pyplot as plt

mu0 = [3, 5, 2]
mu1 = [1, 7, 3]
sigma0= [1, 2, 2]
sigma1 = [3, 2, 1]

N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков – длина массива средних
class0 = np.random.normal(mu0[0],sigma0[0],[N,1]) # инициализируем первый столбец (в Python нумерация от 0)
class1 = np.random.normal(mu1[0],sigma1[0],[N,1])
for i in range(1,col): # подумайте, почему нумерация с 1, а не с 0
    v0 = np.random.normal(mu0[i],sigma0[i],[N,1])
    class0 = np.hstack((class0,v0))
    v1 = np.random.normal(mu1[i],sigma1[i],[N,1])
    class1 = np.hstack((class1,v1))
    
Y1 = np.ones((N, 1), dtype=bool)# массив логических единиц
Y0 = np.zeros((N, 1), dtype=bool)
X = np.vstack((class0,class1))
Y = np.vstack((Y0,Y1)).ravel() #ravel позволяет сделать массив плоским –одномерным, размера (N,), это необходимо для дальнейшего использования вклассификаторах

rng = np.random.default_rng()
arr = np.arange(2*N) #индексы для перемешивания
rng.shuffle(arr)
44
X = X[arr]
Y = Y[arr]

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
    plt.title("Гистограмма №{}".format(i))
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

