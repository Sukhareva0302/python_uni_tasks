import pandas as pd
import matplotlib.pylab as plt
df = pd.read_csv('diabetes_data_upload.csv')
tableYes=df[df['Obesity']=='Yes'] #since there is no 21 colunm, I choose 15
tableNo=df[df['Obesity']=='No']
plt.subplot(1, 2, 1)
plt.title('Age for only Yes')
plt.boxplot(tableYes.iloc[:,0])
plt.subplot(1, 2, 2)
plt.title('Age for only No')
plt.boxplot(tableNo.iloc[:,0])
plt.show()
