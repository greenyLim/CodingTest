-- 코드를 입력하세요
SELECT i.animal_id, i.animal_type, i.name
from animal_ins i
join animal_outs o
On i.animal_id=o.animal_id
where i.SEX_UPON_INTAKE like 'intact%'
and o.SEX_UPON_OUTCOME not like 'intact%'