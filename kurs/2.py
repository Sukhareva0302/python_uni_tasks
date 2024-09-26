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


def buildHistplot(data, className):
    idx = 0
    for col in data.columns:
        try:
            data[col].plot.kde(alpha=0.5, stacked=True)  # hist

            if ((idx % 12 == 0 or idx == len(data.columns)) and idx != 0):
                # Plot formatting
                plt.rcParams["figure.figsize"] = (10, 10)
                plt.legend(prop={'size': 10}, title='legend')
                plt.title('График распределения параметров для класса {}'.format(className))
                plt.grid()
                plt.xlabel('Значение (min)')
                plt.ylabel('Плотность')
                plt.show()
        except:
            pass
        idx += 1
def buildHistplot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    plt.legend(('Gender','self_employed','family_history',
               'treatment','Days_Indoors','Growing_Stress','Changes_Habits',
                'Mental_Health_History','Mood_Swings','Coping_Struggles',
                'Work_Interest','Social_Weakness','mental_health_interview',
                'care_options'))
    plt.subplot(1,2,1)
    plt.title('График распределения для класса {} выше медианы'.format(className))
    plt.hist(higher)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    #plt.show()
    plt.subplot(1,2,2)
    plt.title('График распределения для класса {} ниже медианы'.format(className))
    plt.legend(('Gender','self_employed','family_history',
               'treatment','Days_Indoors','Growing_Stress','Changes_Habits',
                'Mental_Health_History','Mood_Swings','Coping_Struggles',
                'Work_Interest','Social_Weakness','mental_health_interview',
                'care_options'))
    plt.hist(below)
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
sns.displot(df_data, kind="kde").set (title='График распределения выборки')
plt.show()
print("Всего элементов в датесете =", len(df_data), "\n")

temp=np.array([])
temp2=np.array([])
for i in range(0, len(df_data.columns)):
               sorted_values = df_data.iloc[:,i].sort_values()
               temp2=np.append(temp, sorted_values)
               temp=np.append(temp, sorted_values.index[len(sorted_values) // 2])
median_value=round(sum(temp)/len(temp))
print("Медиана для всего датасета = ", median_value)
sorted_values1 = df_data['Coping_Struggles'].sort_values()
median_value1 = sorted_values1.index[len(sorted_values1) // 2]
print("Медиана для класса 1 'Coping_Struggles' = ", median_value1)

sorted_values2 = df_data['Growing_Stress'].sort_values()
median_value2 = sorted_values2.index[len(sorted_values) // 2]
print("Медиана для класса 2 'Growing_Stress' = ", median_value2)

sorted_values3 = df_data['treatment'].sort_values()
median_value3 = sorted_values3.index[len(sorted_values) // 2]
print("Медиана для класса 3 'treatment'= ", median_value3,"\n")

buildHistplot_median(df_data, median_value1, "Coping_Struggles")
buildHistplot_median(df_data, median_value2, "Growing_Stress")
buildHistplot_median(df_data, median_value3, "treatment")

print("Данные после преобработки\n", df_data)
print("Данные класса 1\n", df_data1)
print("Данные класса 2\n", df_data2)
print("Данные класса 3\n", df_data3)

buildHistplot(df_data, "Вся выборка")
buildHistplot(df_data1, "Coping_Struggles")
buildHistplot(df_data2, "Growing_Stress")
buildHistplot(df_data3, "treatment")

#buildPlot(df_data.T, "Вся выборка") - it will kill ALL


