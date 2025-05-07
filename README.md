# Бонусное задание по базам данных

---
## Вариант 6

Вариант = ([Номер первой буквы фамилии] + [Номер первой буквы имени] + [Номер второй буквы логина Telegram] ) mod 7 + 1

p.s. латиница

* Smirnova - S - 19
* Maria - M - 13
* @maria_smrnv - 1

(S + M + A) = (19 + 13 + 1) = 33

33 mod 7 = 5

5 + 1 = 6

Вариант = 6 

---

## Условия задания

Предложены данные **Brazilian E-Commerce Public Dataset by Olist**. Набор данных содержит информацию о 100 тысячах заказов с 2016 по 2018 год, сделанных на торговых площадках Бразилии.

Схема таблиц с [официального описания](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce):

![alt text](image.png)

### Задачи:

1. Проанализируйте для города Белу-Оризонти распределение товаров электроника, мебель, игрушки по месяцам и объясните с чем это связано.

2. Определите категории товаров, которые чаще всего попадают в отмененные заказы штата Рио-де-Жанейро.

3. Определите средний чек клиента для штатов Сан-Паулу и Пернамбуку.

4. Исследуйте долю пользователей, которые с момента первого заказа в течение 30 дней совершили еще один заказ.

---

## Структура работы

```
.
├── README.md
├── image.png                              # диаграмма БД
├── analysis
│   └── analysis.ipynb                     # Jupyter Notebook с анализом 
├── csv_tables                             # Данные Olist
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
├── results                               
│   ├── task1_images                       # Графики и визуализации
│   │   ├── electronics.png
│   │   ├── furniture_bedroom.png
│   │   ├── furniture_decor.png
│   │   ├── furniture_living_room.png
│   │   ├── furniture_mattress_and_upholstery.png
│   │   ├── kitchen_dining_laundry_garden_furniture.png
│   │   ├── office_furniture.png
│   │   └── toys.png
│   ├── task2_images
│   │   ├── cancelled_categories_rj.png
│   │   └── cancelled_categories_rj_2.png
│   └── task4_images
│       └── repeaters_30d.png                                
│   ├── task1.txt                          # Результаты SQL-запросов  
│   ├── task1_1.txt
│   ├── task2_v1.txt
│   ├── task2_v2.txt
│   ├── task3.txt
│   ├── task4.txt
│   └── task4_new.txt
├── src                                    # SQL и Python скрипты
│   ├── create_database.sql                # Создание базы данных
│   ├── create_tables.py                   # Создание таблиц (Python)
│   ├── task1.py
│   ├── task1.sql
│   ├── task1_1.sql
│   ├── task2_stat.py
│   ├── task2_v1.py
│   ├── task2_v1.sql
│   ├── task2_v2.py
│   ├── task2_v2.sql
│   ├── task3.sql
│   ├── task4.py
│   └── task4.sql

```

---