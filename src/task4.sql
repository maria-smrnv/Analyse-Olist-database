WITH first_order AS (
    SELECT
        c.customer_unique_id as customer_uid,
        MIN(o.order_purchase_timestamp::timestamp) AS first_order_date
    FROM olist_customers_dataset c
    JOIN olist_orders_dataset o ON o.customer_id = c.customer_id
    GROUP BY customer_unique_id
    ORDER BY first_order_date
),
second_order AS (
    SELECT
        f.customer_uid,
        f.first_order_date,
        MIN(o.order_purchase_timestamp::timestamp) AS second_order_date
    FROM first_order f
    JOIN olist_customers_dataset c ON 
        c.customer_unique_id = f.customer_uid
    JOIN olist_orders_dataset o ON 
        o.customer_id = c.customer_id
        AND o.order_purchase_timestamp::timestamp > f.first_order_date::timestamp
        AND o.order_purchase_timestamp::timestamp <= f.first_order_date::timestamp + INTERVAL '30 days'
    GROUP BY 
        f.customer_uid,
        f.first_order_date
)
SELECT
    TO_CHAR(f.first_order_date, 'YYYY-MM') AS order_month,
    COUNT(DISTINCT f.customer_uid)  AS count_customers,
    COUNT(DISTINCT s.customer_uid)  AS repeaters_30d,
    ROUND(100.0 * COUNT(DISTINCT s.customer_uid) /
        NULLIF(COUNT(DISTINCT f.customer_uid), 0), 2) AS pct_repeat_within_30d
FROM first_order f
LEFT JOIN second_order s ON f.customer_uid = s.customer_uid
GROUP BY 1
ORDER BY 1;