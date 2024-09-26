import numpy as np
def sigmoid(Z): #сигмоида
    return 1/(1+np.exp(-Z))

def sigmoid_derivative(p): #производная сигмоиды
    return p * (1 - p)
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        n_inp = self.input.shape[1] # кол-во входов
        n_neuro = 4 # число нейронов на главном слое
        # инициализация весов рандомными значениями
        self.weights1= np.random.rand(n_inp,n_neuro)
        self.weights2 = np.random.rand(n_neuro,1)
        self.y = y
        self.output = np. zeros(y.shape)
    def feedforward(self):
        #выходы слоёв вычисляются по сигмоиде
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
    def feedforward_test(self,X):
        #выходы слоёв вычисляются по сигмоиде
        self.layer1 = sigmoid(np.dot(X, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)
                            *sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot
                            (2*(self.y -self.output)*sigmoid_derivative(self.output),
                             self.weights2.T)*sigmoid_derivative(self.layer1))
        #обновляем веса
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        #весь процесс обучения прост – высчитываем выход с помощью прямого
        #распространения, а после обновляем веса
        self.output = self.feedforward()
        self.backprop()
