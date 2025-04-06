-- 코드를 입력하세요
with union_temp as (SELECT online_sale_id as sale_id, user_id, sales_date, product_id, sales_amount
from online_sale 
union all
select offline_sale_id as sale_id, null as user_id, sales_date, product_id, sales_amount
from offline_sale)

select date_format(sales_date,'%Y-%m-%d') as sales_date, product_id, ifnull(user_id,null) as user_id, sales_amount
from union_temp
where sales_date between '2022-03-01' and '2022-03-31'
order by sales_date, product_id, user_id