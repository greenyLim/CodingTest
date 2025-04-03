-- 코드를 입력하세요  distinct(c.car_id)
with temp as (select *
             from car_rental_company_rental_history
             where (start_date between '2022-10-01' and '2022-10-31') )

SELECT distinct(c.car_id) as car_id
from car_rental_company_car c
join temp t on c.car_id=t.car_id
where car_type = '세단' 
order by c.car_id desc