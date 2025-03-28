-- 코드를 입력하세요
SELECT b.category , sum(s.sales) as total_sales
from book b
join book_sales s on b.book_id=s.book_id
where s.sales_date between "2022-01-01" and "2022-01-31"
group by b.category
order by b.category
