import pandas as pd
import numpy as np
from scipy.stats import norm

df = pd.read_csv('C:/lab bd/results/task2_v2.txt', sep='\t', encoding='utf-8')
df.columns = ['category', 'cancelled_count', 'total_orders', 'cancel_rate_percent']

# Общая средняя доля отмен (по всем категориям)
p_global = df['cancelled_count'].sum() / df['total_orders'].sum()

# Вычисление z-статистики и p-value для z-теста 
def z_test(row):
    p_cat = row['cancel_rate_percent'] / 100
    n = row['total_orders']
    se = (p_global * (1 - p_global) / n) ** 0.5
    z = (p_cat - p_global) / se
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return pd.Series([z, p_value])

df[['z_score', 'p_value']] = df.apply(z_test, axis=1)

# Добавим значимость
df['significant_5%'] = df['p_value'] < 0.05
significant = df[df['significant_5%']]

# Сортировка по p-value
significant = significant.sort_values('p_value')
print(significant[['category', 'cancel_rate_percent', 'z_score', 'p_value', 'significant_5%']])