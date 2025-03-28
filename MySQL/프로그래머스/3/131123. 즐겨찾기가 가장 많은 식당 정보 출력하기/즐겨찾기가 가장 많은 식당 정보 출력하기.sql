-- 코드를 입력하세요
with group_max as (select food_type
                   from rest_info
                   group by food_type
                  having favorites= max(favorites))
                   
SELECT food_type, rest_id, rest_name, favorites
from rest_info
where (food_type, favorites) in (select food_type, max(favorites) as favorite
                   from rest_info
                   group by food_type)
order by food_type desc