-- Active: 1738849898400@@127.0.0.1@5432@lab
-- Выведем как в нашей схеме называет Белу-Оризонти
select DISTINCT customer_city
from olist_customers_dataset
where customer_city like 'belo%';
-- Получили belo horizonte