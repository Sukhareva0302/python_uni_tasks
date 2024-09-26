import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame as df
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
pd.set_option('display.max_columns', None)
def preprocessing(r_data):
    df_data=r_data[['Gender', 'family_history', 'treatment', 'Growing_Stress', 'Changes_Habits', 'Mental_Health_History', 'Mood_Swings', 'Coping_Struggles']].copy()
    df_data['Gender']=df_data['Gender'].apply(lambda x: 1 if x=='Male' else 0)
    df_data['family_history']=df_data['family_history'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['treatment']=df_data['treatment'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['Growing_Stress']=df_data['Growing_Stress'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['Changes_Habits']=df_data['Changes_Habits'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['Mental_Health_History']=df_data['Mental_Health_History'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['Mood_Swings']=df_data['Mood_Swings'].apply(lambda x: 1 if x=='Yes' else 0)
    df_data['Coping_Struggles']=df_data['Coping_Struggles'].apply(lambda x: 1 if x=='Yes' else 0)
    return df_data
def buildPlot(data, className):
    plt.plot(data)
    plt.title('График распределения параметров для класса {}'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

def buildHistplot(data, className):
    #scatter_matrix(higher, diagonal="hist")
    sns.histplot(data).set(title='Гистограма для класса {}'.format(className))
    plt.legend(labels=data.columns)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    
def buildBoxplot(data, className):
    sns.boxplot(data).set(title='Боксплот для класса {}'.format(className))
    plt.grid()
    #plt.legend(labels=data.columns)
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    
def buildScatterplot(data, className):
    sns.scatterplot(data).set(title='Скатерограмма для класса выше медианы'.format(className))
    plt.legend(labels=data.columns)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()




#START
#ситываем данные
data = pd.DataFrame(pd.read_csv("Mental Health Dataset.csv"))

#разбиение данных на классы и подготовка данных для дальнейшей работы

df_data = preprocessing(data)
df_data1=df_data.loc[df_data[df_data.columns[1]]==1]
df_data2=df_data.loc[df_data[df_data.columns[2]]==1]
df_data3=df_data.loc[df_data[df_data.columns[3]]==1]

df_data4=df_data.loc[df_data[df_data.columns[0]]==1]
df_data5=df_data.loc[df_data[df_data.columns[0]]==0]

df_data6=df_data.loc[df_data[df_data.columns[3]]==1]
df_data7=df_data.loc[df_data[df_data.columns[4]]==1]
df_data8=data.loc[data[data.columns[6]]=="Yes"]
df_data8=preprocessing(df_data8)
df_data9=df_data.loc[df_data[df_data.columns[7]]==1]


buildBoxplot(df_data6, "Growing_Stress")
buildBoxplot(df_data7, "Changes_Habits")
buildBoxplot(df_data8, "Mood_Swings")
buildBoxplot(df_data9, "Coping_Struggles")
#график распределения всей выборки и классов
sns.displot(df_data, kind="kde").set (title='График распределения выборки')
plt.show()
sns.displot(df_data4, kind="kde").set (title='График распределения класс Gender=male')
plt.show()
sns.displot(df_data5, kind="kde").set (title='График распределения класс Gender=female')
plt.show()


#гистограмма
buildHistplot(df_data, "All")
buildHistplot(df_data1, "family_history")
buildHistplot(df_data2, "treatment")
buildHistplot(df_data3, "Mental_Health_History")
buildHistplot(df_data4, "Gender=male")
buildHistplot(df_data5, "Gender=female")
buildHistplot(df_data6, "Growing_Stress")
buildHistplot(df_data7, "Changes_Habits")
buildHistplot(df_data8, "Mood_Swings")
buildHistplot(df_data9, "Coping_Struggles")


#боксплот
buildBoxplot(df_data, "All")
buildBoxplot(df_data1, "family_history")
buildBoxplot(df_data2, "treatment")
buildBoxplot(df_data3, "Mental_Health_History")
buildBoxplot(df_data4, "Gender=male")
buildBoxplot(df_data5, "Gender=female")


#как выглядят считанные данные
print("Считанный Mental Health датасет\n", data, "\n", data.shape)

#как выглядят данные с которыми работаем
print("Данные после преобработки\n", df_data)
#print("Данные класса 1\n", df_data1)
#print("Данные класса 2\n", df_data2)
#print("Данные класса 3\n", df_data3)


print("Всего элементов в датесете =", len(df_data))
print("Всего элементов в классе 1 'Coping_Struggles' =", len(df_data1))
print("Всего элементов в классе 2 'Growing_Stress' =", len(df_data2))
print("Всего элементов в классе 3 'treatment' =", len(df_data3), "\n")
print("Всего элементов в классе 4 'Gender=male' =", len(df_data4), "\n")
print("Всего элементов в классе 5 'Gender=female' =", len(df_data5), "\n")

#средние значения & стандартное отклонения
print("\nСредние значения для всего датасета = ",
          sum(df_data.mean()) / len(df_data.mean()))
print("\nСредние значения для класса 1 датасета = \n", df_data1.mean(), "\n")
print("Средние значения для класса 2 датасета = \n", df_data2.mean(), "\n")
print("Средние значения для класса 3 датасета = \n", df_data3.mean(), "\n")

print("Стандартное отклонение для всего датасета = ",
          sum(df_data.std()) / len(df_data.std()))
print("Стандартное отклонение для класса 1 датасета = \n", df_data1.std(), "\n")
print("Стандартное отклонение для класса 2 датасета = \n", df_data2.std(), "\n")
print("Стандартное отклонение для класса 3 датасета = \n", df_data3.std(), "\n")

#средние значения & стандартное отклонения param n&m
print(
        "Оценим средние значения для всей выборки и для каждого класса для n параметра {}\n".format(df_data.columns[0]),
        "All=",df_data[df_data.columns[0]].mean(), "\n class 1=", df_data1[df_data1.columns[0]].mean(), "\n class 2=",
        df_data2[df_data2.columns[0]].mean(),"\n class 3=", df_data3[df_data3.columns[0]].mean())
print("Оценим стандартное отклонения для всей выборки и для каждого класса для m параметра {}\n".format(df_data.columns[1]),
        "All=",df_data[df_data.columns[1]].std(), "\n class 1=", df_data1[df_data1.columns[1]].std(), "\n class 2=",
        df_data2[df_data2.columns[1]].std(),"\n class 3=",df_data3[df_data3.columns[1]].std())



