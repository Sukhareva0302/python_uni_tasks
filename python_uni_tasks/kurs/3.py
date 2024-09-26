import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame as df
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

def preprocessing(r_data):
    r_data = r_data.drop('Timestamp', axis=1)
    r_data = r_data.drop('Country', axis=1)
    r_data = r_data.drop('Occupation', axis=1)
    df_preprocessing_data = r_data.drop('Days_Indoors', axis=1)
    for column in df_preprocessing_data:
        if df_preprocessing_data[column].dtypes == object:
            variants = list(set(df_preprocessing_data[column]))
            df_preprocessing_data[column] = [variants.index(i) for i in df_preprocessing_data[column]]
    return df_preprocessing_data
def buildPlot(data, className):
    plt.plot(data)
    plt.title('График распределения параметров для класса {}'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

def buildPlot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    plt.subplot(1,2,1)
    sns.displot(higher, kind="kde").set(title='График распределения для класса {} выше медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.subplot(1,2,2)
    sns.displot(below, kind="kde").set(title='График распределения для класса {} ниже медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    
def buildHistplot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    plt.subplot(1,2,1)
    sns.histplot.set(title='График распределения для класса {} выше медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.subplot(1,2,2)
    sns.histplot(below).set(title='График распределения для класса {} ниже медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

data = pd.DataFrame(pd.read_csv("Mental Health Dataset.csv"))
print("Считанный Mental Health датасет\n", data, "\n", data.shape)

class1=data.loc[data[data.columns[12]]=='Yes']#Coping_Struggles
class2=data.loc[data[data.columns[8]]=='Yes']#Growing_Stress
class3=data.loc[data[data.columns[6]]=='Yes']#treatment
df_data = preprocessing(data)
df_data1 = preprocessing(class1)
df_data2 = preprocessing(class2)
df_data3 = preprocessing(class3)

class_n=data.loc[data[data.columns[1]]=='Female']#Gender=Female
class_m=data.loc[data[data.columns[4]]=='Yes']#self_employed
df_data_n = preprocessing(class_n)
df_data_m = preprocessing(class_m)

sorted_values = df_data['Gender'].sort_values()
median_value_n = sorted_values.index[len(sorted_values) // 2]
sorted_values = df_data['Gender'].sort_values()
median_value_m = sorted_values.index[len(sorted_values) // 2]
#median_value=df_data['Gender'].median().index
print("Медиана для всего датасета по n и m= ", median_value_n, median_value_m)


print("Данные после преобработки\n", df_data)
print("Данные класса 1\n", df_data1)
print("Данные класса 2\n", df_data2)
print("Данные класса 3\n", df_data3)
sns.displot(df_data, kind="kde").set (title='График распределения выборки')
plt.show()
sns.displot(df_data1, kind="kde").set (title='График распределения класс Coping_Struggles')
plt.show()
sns.displot(df_data2, kind="kde").set (title='График распределения класс Growing_Stress')
plt.show()
sns.displot(df_data3, kind="kde").set (title='График распределения класс treatment')
plt.show()

print("Всего элементов в датесете =", len(df_data), "\n")

"""temp=np.array([])
for i in range(0, len(df_data.columns)):
               sorted_values = df_data.iloc[:,i].sort_values()
               temp=np.append(temp, sorted_values.index[len(sorted_values) // 2])
median_value=round(sum(temp)/len(temp))
"""
sorted_values = df_data['Gender'].sort_values()
median_value_n = sorted_values.index[len(sorted_values) // 2]
sorted_values = df_data['Gender'].sort_values()
median_value_m = sorted_values.index[len(sorted_values) // 2]
#median_value=df_data['Gender'].median().index
print("Медиана для всего датасета по n и m= ", median_value_n, median_value_m)

"""
temp=np.array([])
for i in range(0, len(df_data1.columns)):
               sorted_values = df_data1.iloc[:,i].sort_values()
               temp=np.append(temp, sorted_values.index[len(sorted_values) // 2])
"""
median_value1=df_data1['Gender'].median()
print("Медиана для класса 1 'Coping_Struggles' = ", median_value1)

"""
temp=np.array([])
for i in range(0, len(df_data2.columns)):
               sorted_values = df_data2.iloc[:,i].sort_values()
               temp=np.append(temp, sorted_values.index[len(sorted_values) // 2])
"""
median_value2=df_data2['Gender'].median()
print("Медиана для класса 2 'Growing_Stress' = ", median_value2)

"""
temp=np.array([])
for i in range(0, len(df_data3.columns)):
               sorted_values = df_data3.iloc[:,i].sort_values()
               temp=np.append(temp, sorted_values.index[len(sorted_values) // 2])
"""
median_value3=df_data3['Gender'].median()
print("Медиана для класса 3 'treatment'= ", median_value3,"\n")

buildPlot_median(df_data, median_value, "All")
buildPlot_median(df_data1, median_value1, "Coping_Struggles")
buildPlot_median(df_data2, median_value2, "Growing_Stress")
buildPlot_median(df_data3, median_value3, "treatment")

buildHistplot_median(df_data, median_value, "All")
buildHistplot_median(df_data1, median_value1, "Coping_Struggles")
buildHistplot_median(df_data2, median_value2, "Growing_Stress")
buildHistplot_median(df_data3, median_value3, "treatment")

print("Данные после преобработки\n", df_data)
print("Данные класса 1\n", df_data1)
print("Данные класса 2\n", df_data2)
print("Данные класса 3\n", df_data3)

#buildPlot(df_data.T, "Вся выборка") - it will kill ALL


