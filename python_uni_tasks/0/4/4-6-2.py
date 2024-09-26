import pandas as pd
import matplotlib.pylab as plt
table = pd.read_csv('diabetes_data_upload.csv')
tableYes=table[table['Obesity']=='Yes'] #since there is no 21 colunm, I choose 15
tableNo=table[table['Obesity']=='No']

plt.subplot(1, 2, 1)
plt.title('Age for only Yes')
plt.hist(tableYes.iloc[:,0])
plt.subplot(1, 2, 2)
plt.title('Age for only No')
plt.hist(tableNo.iloc[:,0])
plt.show()
