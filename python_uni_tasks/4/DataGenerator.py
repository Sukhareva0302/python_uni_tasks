import numpy as np
from sklearn.datasets import make_moons

def norm_dataset(mu,sigma,N): # обозначение имя функции и входныхаргументов
    mu0 = mu[0]
    mu1 = mu[1]
    sigma0= sigma[0]
    sigma1 = sigma[1]
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
    X = X[arr]
    Y = Y[arr]

    return X, Y, class0, class1 # возвращаемые аргументы

def norm_dataset_N(mu,sigma,N):
    
    X, Y = make_moons(n_samples=N*2, random_state=1, noise=0.1)
    rng = np.random.default_rng()
    arr = np.arange(2*N) #индексы для перемешивания
    rng.shuffle(arr)
    X = X[arr]
    Y = Y[arr]
    return X, Y
