# -*- coding: utf-8 -*-
"""
Давлетбирдин БС/б-19-1-о | Вариант - 3

"""

import pylab
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
import scipy.stats as stats

# Импорт данных
Gt = np.loadtxt('C:/student/Gt.txt')
H = np.loadtxt('C:/student/H.txt')
Mk = np.loadtxt('C:/student/Mk.txt')
Pa = np.loadtxt('C:/student/Pa.txt')

#                     Числовые характеристики

# Расчет дисперсии
Disp = [(st.variance(Gt), st.variance(H), st.variance(Mk), st.variance(Pa))]
print('Дисперсия для заданных процессов:', Disp)
print()

# Расчет стандартного отклонения
Sto = [(st.pstdev(Gt), st.pstdev(H), st.pstdev(Mk), st.pstdev(Pa))]
print('Стандартное отклонение заданных процессов:', Sto)
print()

# Среднее значение
Avrg = [st.mean(Gt), st.mean(H), st.mean(Mk), st.mean(Pa)]
print('Среднее значение для заданных процессов:', Avrg)
print()
#                     Функциональные характеристики

# Построение гистограмм. 
GtF = sns.distplot(Gt,bins=50,kde=True,color='red',
                  hist_kws={'alpha':1})
GtF.set(xlabel='Нормальное распределение', ylabel='Частота')

HF = sns.distplot(H,bins=50,kde=True,color='green',
                  hist_kws={'alpha':1})
HF.set(xlabel='Нормальное распределение', ylabel='Частота')

MkF = sns.distplot(Mk,bins=50,kde=True,color='blue',
                  hist_kws={'alpha':1})
MkF.set(xlabel='Нормальное распределение', ylabel='Частота')

PaF = sns.distplot(Pa,bins=50,kde=True,color='yellow',
                  hist_kws={'alpha':1})
PaF.set(xlabel='Нормальное распределение', ylabel='Частота')
plt.show()

