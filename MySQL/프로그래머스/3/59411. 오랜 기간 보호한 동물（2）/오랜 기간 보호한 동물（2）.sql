-- 코드를 입력하세요
SELECT o.animal_id, o.name 
from animal_ins i 
right join animal_outs o on i.animal_id=o.animal_id
order by o.datetime-i.datetime desc
limit 2