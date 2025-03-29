-- 코드를 입력하세요
with july_group as (select flavor, sum(total_order) as total
                   from july
                   group by flavor)

SELECT f.flavor
from first_half f
join july_group j on f.flavor=j.flavor
order by (f.total_order + j.total) desc
limit 3