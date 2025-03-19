-- 코드를 작성해주세요
select d.id, d.email, d.first_name, d.last_name
from developers d
where d.skill_code & (select s.code from skillcodes s where name = 'Python') or
        d.skill_code & (select s.code from skillcodes s where name = 'C#') 
order by d.id