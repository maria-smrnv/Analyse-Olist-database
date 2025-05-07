import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# Подключение к базе данных
engine = create_engine("postgresql://postgres:12345@localhost:5432/lab")

with open('C:/lab bd/src/task2_v1.sql', 'r', encoding='utf-8') as f:
    query = f.read()

with engine.connect() as conn:
    df = pd.read_sql_query(text(query), conn)

df.columns = ['category', 'cancelled_count', 'percentage']

# Категории >= 3%
df_main = df[df['percentage'] >= 3].copy()

# Категории <= 3%
df_others = df[df['percentage'] < 3].copy()
if not df_others.empty:
    others_row = pd.DataFrame({
        'category': ['Others'],
        'cancelled_count': [df_others['cancelled_count'].sum()],
        'percentage': [df_others['percentage'].sum()]
    })
    df_main = pd.concat([df_main, others_row], ignore_index=True)


df_main = df_main.sort_values('percentage', ascending=False)

# Цвета из табличной палитры tab20
colors = plt.get_cmap('tab20').colors[:len(df_main)]


# Создание подписи для легенды
legend_labels = [f"{row['category']}" for _, row in df_main.iterrows()]

# Построение круговой диаграммы
plt.figure(figsize=(10, 6))
wedges, _, _ = plt.pie(
    df_main['cancelled_count'],
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
)

# Легенда сбоку
plt.legend(wedges, legend_labels, title="Категории", loc="center left", bbox_to_anchor=(1, 0.5))

plt.title('Категории с отменами в штате Рио-де-Жанейро по абсолютному значению')
plt.axis('equal')
plt.tight_layout()


plt.savefig('C:/lab bd/results/task2_images/cancelled_categories_rj.png', dpi=300, bbox_inches='tight')
