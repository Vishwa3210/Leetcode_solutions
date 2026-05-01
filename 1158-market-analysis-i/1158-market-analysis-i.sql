# Write your MySQL query statement below
select  u.user_id as buyer_id,
u.join_date as join_date, 
COUNT(CASE WHEN YEAR(o.order_date) = 2019 THEN o.item_id END) AS orders_in_2019
from users u 
left join orders o
on u.user_id=o.buyer_id

group by u.user_id
order by u.user_id