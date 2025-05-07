import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/lab"
)

files = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]

for file in files:
    df = pd.read_csv(f'C:\lab bd\data\{file}')
    table_name = file.replace('.csv', '')
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')
