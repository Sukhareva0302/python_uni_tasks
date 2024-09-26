import numpy as np
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

"""
Функция предобработки данных.
"""

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


"""
Функция вывода графического распределения параметров. Выводится по 5 датчиков на график.
"""

def buildHistplot_23(data, className):
    idx = 0
    for col in data.columns:
        try:
            data[col].plot.kde(alpha=0.5, stacked=True)  # hist

            if ((idx % 5 == 0 or idx == len(data.columns)) and idx != 0):
                # Plot formatting
                plt.rcParams["figure.figsize"] = (10, 10)
                plt.legend(prop={'size': 10}, title='sensors')
                plt.title('График распределения параметров для класса {}'.format(className))
                plt.grid()
                plt.xlabel('Значение (min)')
                plt.ylabel('Плотность')
                plt.show()
        except:
            pass
        idx += 1



"""
Функция разделения данных по медиане.
"""


def splitByMediana(data, mediana):
    below = []
    higher = []

    for col in data.columns:
        below.append([i for i in data[col] if i < mediana])
        higher.append([i for i in data[col] if i > mediana])

    below = sum(below, [])
    higher = sum(higher, [])

    if len(below) < len(higher):
        below = below + [0] * (len(higher) - len(below))
    elif len(higher) < len(below):
        higher = higher + [0] * (len(below) - len(higher))

    return df({"below": below, "higher": higher})


"""
Функция вывода графического распределения параметров по медиане.
"""


def buildHistplot_45(data, medians, className):
    tmp_df = splitByMediana(data, medians)

    try:
        tmp_df.plot.kde(alpha=0.5, stacked=True)  # hist

        # Plot formatting
        plt.rcParams["figure.figsize"] = (10, 10)
        # plt.legend(prop={'size': 10}, title='sensors')
        plt.title('График распределения для класса {} выше и ниже медианы'.format(className))
        plt.grid()
        plt.xlabel('Значение (min)')
        plt.ylabel('Плотность')
        plt.show()
    except:
        pass


"""
Функция вывода box по медиане. 
"""


def buildBoxplot_5(data, medians, className):
    tmp_df = splitByMediana(data, medians)

    try:
        tmp_df.plot.box()  # kde

        # Plot formatting
        plt.rcParams["figure.figsize"] = (10, 10)
        # plt.legend(prop={'size': 10}, title='sensors')
        plt.title('Boxplot для класса {} выше и ниже медианы'.format(className))
        plt.grid()
        plt.show()
    except:
        pass


"""
Функция вывода скатерограммы параметров по медиане.
"""


def buildScatter_5(data, medians, className):
    tmp_df = splitByMediana(data, medians)

    try:
        scatter_matrix(tmp_df, diagonal="hist")

        # Plot formatting
        plt.rcParams["figure.figsize"] = (10, 10)
        # plt.legend(prop={'size': 10}, title='sensors')
        plt.title('Скатерограмма для класса {} выше и ниже медианы'.format(className))
        plt.grid()
        plt.show()
    except:
        pass


if __name__ == '__main__':
    data = pd.DataFrame(pd.read_csv("Mental Health Dataset.csv"))
    print("Считанный Mental Health Dataset датасет\n", data, "\n", data.shape)

    df_preprocessing_data = preprocessing(data)
    print("Данные после преобработки\n", df_preprocessing_data)

    df_class1, df_class2, df_class3 = np.array_split(df_preprocessing_data, 3)

    """
    1
    """
    buildHistplot_23(df_class1, "class_1")
    buildHistplot_23(df_class2, "class_2")
    buildHistplot_23(df_class3, "class_3")

    """
    2-3
    """


    def calculate_mediana(m_data):
        tmp = m_data.to_numpy().ravel()
        tmp = np.sort(tmp)
        tmp_med = tmp[round(len(tmp) / 2)] if len(tmp) % 2 == 1 else (tmp[int(len(tmp) / 2)] + tmp[
            int(len(tmp) / 2 + 1)]) / 2
        return tmp_med


    print("Медиана для всего датасета = ", calculate_mediana(df_preprocessing_data))
    print("Медиана для класса 1 датасета = ", calculate_mediana(df_class1))
    print("Медиана для класса 2 датасета = ", calculate_mediana(df_class2))
    print("Медиана для класса 3 датасета = ", calculate_mediana(df_class3), "\n")

    """
    4
    """
    buildHistplot_45(df_class1, calculate_mediana(df_class1), "class_1")
    buildHistplot_45(df_class2, calculate_mediana(df_class2), "class_2")
    buildHistplot_45(df_class3, calculate_mediana(df_class3), "class_3")

    """
    5
    """
    buildBoxplot_5(df_class1, calculate_mediana(df_class1), "class_1")
    buildBoxplot_5(df_class1, calculate_mediana(df_class2), "class_2")
    buildBoxplot_5(df_class1, calculate_mediana(df_class3), "class_3")

    buildScatter_5(df_class1, calculate_mediana(df_class1), "class_1")
    buildScatter_5(df_class1, calculate_mediana(df_class2), "class_2")
    buildScatter_5(df_class1, calculate_mediana(df_class3), "class_3")

    """
    6
    """
    print("Средние значения для всего датасета = ",
          sum(df_preprocessing_data.mean()) / len(df_preprocessing_data.mean()))
    print("Средние значения для класса 1 датасета = \n", df_class1.mean(), "\n")
    print("Средние значения для класса 2 датасета = \n", df_class2.mean(), "\n")
    print("Средние значения для класса 3 датасета = \n", df_class3.mean(), "\n")

    print("Стандартное отклонение для всего датасета = ",
          sum(df_preprocessing_data.std()) / len(df_preprocessing_data.std()))
    print("Стандартное отклонение для класса 1 датасета = \n", df_class1.std(), "\n")
    print("Стандартное отклонение для класса 2 датасета = \n", df_class2.std(), "\n")
    print("Стандартное отклонение для класса 3 датасета = \n", df_class3.std(), "\n")

    """
    7-8
    """
    print(
        "Оценим средние значения для каждого класса для третьего параметра {}".format(df_preprocessing_data.columns[2]),
        df_class1[df_class1.columns[2]].mean(), df_class2[df_class2.columns[2]].mean(),
        df_class3[df_class3.columns[2]].mean())
    print("Оценим стандартное отклонения для каждого класса для третьего параметра {}".format(
        df_preprocessing_data.columns[2]),
          df_class1[df_class1.columns[2]].std(), df_class2[df_class2.columns[2]].std(),
          df_class3[df_class3.columns[2]].std())
