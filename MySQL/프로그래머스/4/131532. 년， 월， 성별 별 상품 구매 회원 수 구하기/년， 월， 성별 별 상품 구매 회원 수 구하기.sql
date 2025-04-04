-- 코드를 입력하세요

SELECT year(o.sales_date) as year, month(o.sales_date) as month, 
u.gender, count(distinct(o.user_id)) as users
from user_info u
join online_sale o on u.user_id=o.user_id
where u.gender is not null
group by year, month, gender
order by year, month, gender
