import pandas as pd
import matplotlib.pylab as plt
df = pd.read_csv('diabetes_data_upload.csv')
df1 = df.iloc[:,0:3]
plt.hist(df1.iloc[:,0])
plt.show()
plt.hist(df1.iloc[:,1])
plt.show()
plt.hist(df1.iloc[:,2])
plt.show()
