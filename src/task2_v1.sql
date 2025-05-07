SELECT
    pt.product_category_name_english AS category,
    COUNT(*) AS cancelled_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS "percentage_%"
FROM olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
JOIN olist_products_dataset p ON oi.product_id = p.product_id
JOIN product_category_name_translation pt ON p.product_category_name = pt.product_category_name
WHERE 
    o.order_status = 'canceled' AND c.customer_state = 'RJ'
GROUP BY 
    pt.product_category_name_english
ORDER BY 
    cancelled_count DESC;
