-- 코드를 작성해주세요
select sum(g.score) as score, g.emp_no, e.emp_name, e.position, e.email
from hr_employees e
join hr_grade g 
on e.emp_no=g.emp_no
where year=2022
group by emp_no
order by score desc
limit 1

