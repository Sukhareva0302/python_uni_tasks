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
            print(column, variants)
            for i in df_preprocessing_data[column]:
                print(variants.index(i))
                df_preprocessing_data[column] =[variants.index(i)]
            print('\n')
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
    sns.displot(higher, kind="kde").set(title='График распределения для класса {} выше медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    sns.displot(below, kind="kde").set(title='График распределения для класса {} ниже медианы'.format(className))
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    
def buildHistplot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    #scatter_matrix(higher, diagonal="hist")
    sns.histplot(higher).set(title='Гистограма для класса {} выше медианы'.format(className))
    plt.legend(labels=data.columns)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    sns.histplot(below).set(title='Гистограмма для класса {} ниже медианы'.format(className))
    plt.legend(labels=data.columns)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

def buildScatterplot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    sns.scatterplot(higher).set(title='Скатерограмма для класса {} выше медианы'.format(className))
    plt.legend(labels=data.columns)
    plt.grid()
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    sns.scatterplot(below).set(title='Скатерограмма для класса {} ниже медианы'.format(className))
    plt.grid()
    plt.legend(labels=data.columns)
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

def buildBoxplot_median(data, mediana, className):
    below = data[0:mediana]
    higher = data[mediana:len(data)]
    sns.boxplot(higher).set(title='Боксплот для класса {} выше медианы'.format(className))
    plt.grid()
    plt.legend(labels=data.columns)
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()
    sns.boxplot(below).set(title='Боксплот для класса {} ниже медианы'.format(className))
    plt.grid()
    plt.legend(labels=data.columns)
    plt.xlabel('Значение (min)')
    plt.ylabel('Плотность')
    plt.show()

#START
#ситываем данные
data = pd.DataFrame(pd.read_csv("Mental Health Dataset.csv"))

#разбиение данных на классы и подготовка данных для дальнейшей работы
class1=data.loc[data[data.columns[12]]=='Yes']#Coping_Struggles
class2=data.loc[data[data.columns[8]]=='Yes']#Growing_Stress
class3=data.loc[data[data.columns[6]]=='Yes']#treatment
df_data = preprocessing(data)
df_data1 = preprocessing(class1)
df_data2 = preprocessing(class2)
df_data3 = preprocessing(class3)


#mediana
sorted_values = df_data['Gender'].sort_values()
median_value_n = sorted_values.index[len(sorted_values) // 2]
sorted_values = df_data['self_employed'].sort_values()
median_value_m = sorted_values.index[len(sorted_values) // 2]
#mediana class 1
sorted_values1n = df_data1['Gender'].sort_values()
median_value_n1 = sorted_values1n.index[len(sorted_values1n) // 2]
sorted_values1m = df_data1['self_employed'].sort_values()
median_value_m1 = sorted_values1m.index[len(sorted_values1m) // 2]
#mediana class 2
sorted_values2n = df_data2['Gender'].sort_values()
median_value_n2 = sorted_values2n.index[len(sorted_values2n) // 2]
sorted_values2m = df_data2['self_employed'].sort_values()
median_value_m2 = sorted_values2m.index[len(sorted_values2m) // 2]
#mediana class 3
sorted_values3n = df_data3['Gender'].sort_values()
median_value_n3 = sorted_values3n.index[len(sorted_values3n) // 2]
sorted_values3m = df_data3['self_employed'].sort_values()
median_value_m3 = sorted_values3m.index[len(sorted_values3m) // 2]

print("Всего элементов в датесете =", len(df_data))
print("Всего элементов в классе 1 'Coping_Struggles' =", len(df_data1))
print("Всего элементов в классе 2 'Growing_Stress' =", len(df_data2))
print("Всего элементов в классе 3 'treatment' =", len(df_data3), "\n")


#медианы вывод
print("Медиана для всего датасета по n и m= ", median_value_n,",", median_value_m)

print("Медиана для класса 1 'Coping_Struggles' по n и m= ", median_value_n1,",",  median_value_m1)

print("Медиана для класса 2 'Growing_Stress' по n и m= ", median_value_n2, ",",median_value_m2)

print("Медиана для класса 3 'treatment' по n и m= ", median_value_n3,",", median_value_m3)



#график распределения всей выборки и классов
sns.displot(df_data, kind="kde").set (title='График распределения выборки')
plt.show()
sns.displot(df_data1, kind="kde").set (title='График распределения класс Coping_Struggles')
plt.show()
sns.displot(df_data2, kind="kde").set (title='График распределения класс Growing_Stress')
plt.show()
sns.displot(df_data3, kind="kde").set (title='График распределения класс treatment')
plt.show()


#график распределения (выше и ниже медианы по m и по n в основной выборке)
buildPlot_median(df_data, median_value_n, "All for n param")
buildPlot_median(df_data, median_value_m, "All for m param")

#гистограмма (выше и ниже медианы по m и по n в основной выборке)
buildHistplot_median(df_data, median_value_n, "All for n param")
buildHistplot_median(df_data, median_value_m, "All for m param")

#боксплот (выше и ниже медианы по m и по n в основной выборке)
buildBoxplot_median(df_data, median_value_n, "All for n param")
buildBoxplot_median(df_data, median_value_m, "All for m param")

#скатерограмма (выше и ниже медианы по m и по n в основной выборке)
buildScatterplot_median(df_data, median_value_n, "All for n param")
buildScatterplot_median(df_data, median_value_m, "All for m param")


#как выглядят считанные данные
print("Считанный Mental Health датасет\n", data, "\n", data.shape)

#как выглядят данные с которыми работаем
print("Данные после преобработки\n", df_data)
print("Данные класса 1\n", df_data1)
print("Данные класса 2\n", df_data2)
print("Данные класса 3\n", df_data3)

print("Всего элементов в датесете =", len(df_data), "\n")


#медианы вывод
print("Медиана для всего датасета по n и m= ", median_value_n,",", median_value_m)

print("Медиана для класса 1 'Coping_Struggles' по n и m= ", median_value_n1,",",  median_value_m1)

print("Медиана для класса 2 'Growing_Stress' по n и m= ", median_value_n2, ",",median_value_m2)

print("Медиана для класса 3 'treatment' по n и m= ", median_value_n3,",", median_value_m3)


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



