# Write your MySQL query statement below
SELECT 
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) # find the earliest delivery date for each id and example has different id 
    FROM Delivery
    GROUP BY customer_id
);
