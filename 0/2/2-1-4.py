import numpy as np
import pandas as pd
import sklearn as sk
import tensorflow as tf
import keras

table = pd.read_csv('diabetes_data_upload.csv')
print('Averege age:', table['Age'].mean())
print('Averege age by:', table.groupby('Gender')['Age'].mean())

