# Write your MySQL query statement below
select product_id, (case when store1 then 'store1' else 0 end) as store ,
(case when store1 then store1 else 0 end) as price    
from Products
where store1 is not null

union 
select product_id, (case when store2 then 'store2' else 0 end) as store ,
(case when store2 then store2 else 0 end) as price    
from Products
where store2 is not null

union
select product_id, (case when store3 then 'store3' else 0 end) as store ,
(case when store3 then store3 else 0 end) as price    
from Products
where store3 is not null