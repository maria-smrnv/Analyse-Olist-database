
SELECT
    c.customer_state AS state,
    ROUND(AVG(op.payment_value)::numeric, 2) AS avg_sales_receipt
FROM olist_order_payments_dataset op
JOIN olist_orders_dataset o ON op.order_id = o.order_id
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
WHERE 
    c.customer_state IN ('SP', 'PE')
GROUP BY 
    c.customer_state
ORDER BY 
    avg_sales_receipt DESC;