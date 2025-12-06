# Write your MySQL query statement below
select
round(avg(case when d.order_date=d.customer_pref_delivery_date then 1 else 0 end)*100,2) as immediate_percentage from Delivery d JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) t
ON d.customer_id = t.customer_id
AND d.order_date = t.first_order_date;