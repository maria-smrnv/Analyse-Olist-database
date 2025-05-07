SELECT
    pt.product_category_name_english AS category,
    TO_CHAR(o.order_purchase_timestamp::timestamp, 'YYYY-MM') AS month,
    COUNT(*) AS total_sales
FROM olist_orders_dataset o
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
