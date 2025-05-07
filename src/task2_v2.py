import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# Подключение к базе данных
engine = create_engine("postgresql://postgres:12345@localhost:5432/lab")

with open('C:/lab bd/src/task2_v2.sql', 'r', encoding='utf-8') as f:
    query = f.read()

with engine.connect() as conn:
    df = pd.read_sql_query(text(query), conn)

df.columns = ['category', 'cancelled_count', 'total', 'percentage']

# Категории >= 0.5%
df_main = df[df['percentage'] >= 0.5].copy()

# Категории с процентами < 0.5%
df_others = df[df['percentage'] < 0.5].copy()

# Если есть категории, у которых процент меньше 0.5%, объединяем их в "Others"
if not df_others.empty:
    others_row = pd.DataFrame({
        'category': ['Others'],
        'cancelled_count': [df_others['cancelled_count'].max()],
        'percentage': [df_others['percentage'].max()]
    })
    df_main = pd.concat([df_main, others_row], ignore_index=True)


df_main = df_main.sort_values('percentage', ascending=False)

# Цвета из палитры tab20
colors = plt.get_cmap('tab20').colors[:len(df_main)]

# Построение столбчатой диаграммы
plt.figure(figsize=(12, 7))
plt.barh(df_main['category'], df_main['percentage'], color=colors)

plt.xlabel('Процент отмененных заказов')
plt.ylabel('Категории товаров')
plt.title('Проценты отмененных заказов по категориям в штате Рио-де-Жанейро')
plt.tight_layout()
plt.savefig('C:/lab bd/results/task2_images/cancelled_categories_rj_2.png', dpi=300)
