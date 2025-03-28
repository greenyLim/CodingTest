-- 코드를 작성해주세요
with fe as (select sum(code) as fe_code
           from skillcodes
           group by category
           having category = 'Front End'),
    table1 as (select case 
               when (skill_code & (select fe_code from fe))
               and (skill_code & (select code from skillcodes where name = 'Python')) 
               then 'A'
                when skill_code & (select code from skillcodes where name = 'C#') 
               then 'B'
                when (skill_code & (select fe_code from fe)) 
               and 
               (skill_code & (select code from skillcodes where name ='Python'))=0 
               then 'C'
               else null
               end as grade, id, first_name, last_name, email
               from developers
              )



select grade, id, email
from table1
where grade is not null
order by grade, id