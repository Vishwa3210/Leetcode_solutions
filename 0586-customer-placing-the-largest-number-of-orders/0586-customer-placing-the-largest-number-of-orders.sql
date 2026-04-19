# Write your MySQL query statement below
select t.customer_number from
(select count(order_number) as o, customer_number from Orders group by customer_number) as t
order by t.o desc
limit 1