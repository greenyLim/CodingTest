with thirty as(select car_type, discount_rate
              from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
              where duration_type='30일 이상' and car_type In ('세단','SUV'))


select distinct(a.car_id), a.car_type, 
round((100-(cast(replace(c.discount_rate, '%','') as signed)))/100*30*a.daily_fee,0)
 as fee
from car_rental_company_car a
left join car_rental_company_rental_history b on a.car_id=b.car_id
join thirty c on a.car_type=c.car_type
where a.car_id NOT IN (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE start_date <= '2022-11-30'
      AND end_date >= '2022-11-01'
)
and (100-(cast(replace(c.discount_rate, '%','') as signed)))/100*30*a.daily_fee >= 500000
  and (100-(cast(replace(c.discount_rate, '%','') as signed)))/100*30*a.daily_fee < 2000000

  
order by fee desc, a.car_type, a.car_id desc