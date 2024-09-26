import function as f
import DataGenerator as dg
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
mu0 = [3, 5, 2]
mu1 = [1, 7, 3]
sigma0= [1, 2, 2]
sigma1 = [3, 2, 1]
losses = []
accuraces = []
N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков

mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y,class0, class1 = dg.norm_dataset(mu,sigma,N) #X, Y,class0, class1 = dg.norm_dataset(mu,sigma,N) | X, Y= dg.norm_dataset_N(mu,sigma,N)
Y = np.reshape(Y,[2000,1])


NN = f.NeuralNetwork(X,Y) # инициализируем сетку на наших данных
N_epoch = 50
for i in range(N_epoch):
    
    print ("\n\nfor iteration # " + str(i) + "\n")
    print ("Loss: \n" + str(np.mean(np.square(Y - NN.feedforward()))))
    pred = NN.feedforward_test(X)
    #print(pred)
    pred = pd.DataFrame(pred, columns=['predictions'])
    pred = pred.round().to_numpy()
    tmp_y = np.array([1.0 if i == True else 0.0 for i in Y]).reshape(-1, 1)
    print("Accurace: \n"+str(accuracy_score(pred, tmp_y)))
    losses.append(np.mean(np.square(Y - NN.feedforward())))
    accuraces.append(accuracy_score(pred, tmp_y))
    NN.train(X, Y) #собственно, обучение сети

pred = NN.feedforward()
print('Prediction=', pred)

plt.figure(figsize=(12, 8))
plt.plot(range(len(losses)), losses, 'r')
plt.plot(range(len(accuraces)), accuraces, 'b')
plt.xlabel("Эпоха")
plt.ylabel("Точность и среднекваратические потери")
plt.show()
                     
print("\n Итоговые веса на 1м слое = ", NN.weights1)
print("\n Итоговые веса на 2м слое = ", NN.weights2)
