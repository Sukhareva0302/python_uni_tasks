import numpy as np
import pandas as pd
import sklearn as sk
import tensorflow as tf
import keras

table = pd.read_csv('diabetes_data_upload.csv')
print(table[['Age']])
