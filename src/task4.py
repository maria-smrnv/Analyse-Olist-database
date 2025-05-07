import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# Подключение к базе данных
engine = create_engine("postgresql://postgres:12345@localhost:5432/lab")

with open('C:/lab bd/src/task4.sql', 'r', encoding='utf-8') as f:
    query = f.read()

with engine.connect() as conn:
    df = pd.read_sql_query(text(query), conn)


df['order_month'] = pd.to_datetime(df['order_month'], format='%Y-%m')
df = df.sort_values('order_month')
df = df[df['count_customers'] > 10]

# Строим столбчатую диаграмму
fig, ax = plt.subplots(figsize=(10, 6))
width = 20
ax.bar(df['order_month'],
       df['count_customers'], width=width, label='Всего клиентов', align='edge')
ax.bar(df['order_month'],
       df['repeaters_30d'], width=width, label='Повторные за 30d', align='edge')

ax.set_xlabel('Месяц первого заказа')
ax.set_ylabel('Количество клиентов')
ax.set_title('Повторный заказ в течение 30 дней')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/lab bd/results/task4_images/repeaters_30d.png', dpi=300)
