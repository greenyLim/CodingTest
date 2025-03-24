with record as (
select car_id, count(history_id) as records
from car_rental_company_rental_history
where (month(start_date) between 8 and 10) and year(start_date)=2022
group by car_id
having records>=5)

-- 코드를 입력하세요
SELECT month(start_date) as month, car_id, count(history_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c
where (month(start_date) between 8 and 10) and year(start_date)=2022
and car_id in (select car_id 
                 from record)
group by month, car_id
order by month asc, car_id desc;