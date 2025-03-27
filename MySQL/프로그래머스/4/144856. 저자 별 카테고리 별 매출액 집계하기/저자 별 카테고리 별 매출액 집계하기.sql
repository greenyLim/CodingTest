-- 코드를 입력하세요
with book_sale_group as (select book_id, sales_date, sum(sales) as sales
                         from book_sales
                         where month(sales_date)=1 and year(sales_date)=2022
                         group by book_id)

SELECT b.author_id, a.author_name, b.category, 
sum(g.sales * b.price) as total_sales
from book b
left join author a on b.author_id=a.author_id
right join book_sale_group g on b.book_id=g.book_id
group by b.author_id, b.category
order by b.author_id, b.category desc