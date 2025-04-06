-- 코드를 작성해주세요
with max_length as (Select fish_type, max(length) as length
                   from fish_info
                   group by fish_type
                   having min(length)>10)

select b.id, a.fish_name, b.length
from fish_name_info a 
join fish_info b on a.fish_type=b.fish_type
where (b.fish_type, b.length) in (select fish_type, length
                                 from max_length)
order by id

