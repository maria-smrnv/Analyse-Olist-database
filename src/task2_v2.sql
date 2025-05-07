SELECT
    pt.product_category_name_english AS category,
    COUNT(*) FILTER (WHERE o.order_status = 'canceled') AS cancelled_count,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) FILTER (WHERE o.order_status = 'canceled') * 100.0 / COUNT(*), 2) AS cancel_rate_percent
FROM olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
JOIN olist_products_dataset p ON oi.product_id = p.product_id
JOIN product_category_name_translation pt ON p.product_category_name = pt.product_category_name
WHERE 
    c.customer_state = 'RJ'
GROUP BY 
    pt.product_category_name_english
ORDER BY 
    cancel_rate_percent DESC;
