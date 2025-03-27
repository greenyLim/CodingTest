select o.animal_id, o.name
from animal_ins i
right join animal_outs o
on i.animal_id=o.animal_id
where intake_condition is null
order by o.animal_id