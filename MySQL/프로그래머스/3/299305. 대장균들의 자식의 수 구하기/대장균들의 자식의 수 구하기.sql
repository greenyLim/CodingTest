-- 코드를 작성해주세요
with group_id as (select parent_id, count(*) as child_count
               from ecoli_data
               group by parent_id)
               
               
select e.id, ifnull(g.child_count,0) as child_count
from ecoli_data e
left join group_id g
on e.id=g.parent_id
order by id