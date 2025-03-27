-- 코드를 입력하세요
select i.name, i.datetime
from animal_ins i 
left join animal_outs o on i.animal_id=o.animal_id
where i.animal_id not in (select o.animal_id
                          from animal_outs o)
order by datetime
limit 3
