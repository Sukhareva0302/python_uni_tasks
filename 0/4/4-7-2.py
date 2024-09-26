import pandas as pd
import numpy as np

import matplotlib.pylab as plt
data = pd.read_csv('output1.csv')
pd.plotting.scatter_matrix(data.iloc[:,[0,-2,-1]], c= data["16"].replace(["1","0"],["blue","red"]))
plt.show()
