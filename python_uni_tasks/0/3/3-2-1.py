import numpy as np
def f(a):
    print("Рамер массива: ",a.shape)
    print("Количество осей: ", a.ndim)
    print("Тип элементов массива: ",a.dtype.name)
    print("Размер в байтах каждого элемента: ",a.itemsize)
    print("Общее количество элементов массива: ",a.size)
