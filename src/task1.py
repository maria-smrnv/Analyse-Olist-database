import os
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/lab"
)

query = """
SELECT
    pt.product_category_name_english AS category,
    TO_CHAR(o.order_purchase_timestamp::timestamp, 'YYYY-MM') AS month,
    COUNT(*) AS total_sales
FROM 
    olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
JOIN olist_products_dataset p ON oi.product_id = p.product_id
JOIN product_category_name_translation pt ON pt.product_category_name = p.product_category_name
WHERE 
    c.customer_city = 'belo horizonte' AND 
    pt.product_category_name_english SIMILAR TO '(%electronics%|%furniture%|%toys%)'
GROUP BY 
    pt.product_category_name_english,
    TO_CHAR(o.order_purchase_timestamp::timestamp, 'YYYY-MM')
ORDER BY 
    pt.product_category_name_english,
    TO_CHAR(o.order_purchase_timestamp::timestamp, 'YYYY-MM');

"""

# Загружаем данные
with engine.connect() as conn:
    df = pd.read_sql_query(text(query), conn)

# Убеждаемся, что месяц правильно интерпретирован
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# Определяем общий диапазон месяцев
min_month = df['month'].min().to_period('M').to_timestamp()
max_month = df['month'].max().to_period('M').to_timestamp()
all_months = pd.date_range(start=min_month, end=max_month, freq='MS')

# Для каждой категории периндексируем и заполним нулями
filled = []
for category, sub in df.groupby('category'):
    ts = sub.set_index('month')['total_sales']
    # Периндексируем на полный набор месяцев, заполнив пустые нулями
    ts_full = ts.reindex(all_months, fill_value=0)
    df_full = ts_full.reset_index().rename(columns={
        'index': 'month',
        'total_sales': 'total_sales'
    })
    df_full['category'] = category
    filled.append(df_full)

df_filled = pd.concat(filled, ignore_index=True)


output_dir = "C:\lab bd\results\task1_images"
# Строим и сохраняем графики
for category in df_filled['category'].unique():
    sub = df_filled[df_filled['category'] == category]
    plt.figure(figsize=(10, 5))
    plt.bar(sub['month'].dt.strftime('%Y-%m'), sub['total_sales'])
    plt.title(f"Продажи категории: {category}")
    plt.xlabel("Месяц")
    plt.ylabel("Количество проданных единиц")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    filename = f"{category.replace(' ', '_').lower()}.png"
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()
