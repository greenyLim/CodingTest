with truck as (select a.car_id,a.car_type, b.history_id, a.daily_fee,b.end_date,b.start_date,datediff(b.end_date, b.start_date)+1 as date_diff,
              case when datediff(b.end_date, b.start_date)+1 >=90 then '90일 이상'
              when datediff(b.end_date, b.start_date)+1 >=30 then '30일 이상'
              when datediff(b.end_date, b.start_date)+1 >=7 then '7일 이상'
              else '7일 미만' end as period
              from CAR_RENTAL_COMPANY_CAR a
              join CAR_RENTAL_COMPANY_RENTAL_HISTORY b on a.car_id=b.car_id
              where car_type = '트럭'),
    truck2 as (select *
              from car_rental_company_discount_plan
              where car_type = '트럭')
              
#t.history_id, 
#round(t.daily_fee*t.date_diff*(1-(((ifnull(p.discount_rate,0))/100))),0) as fee
select t.history_id,round(t.daily_fee*t.date_diff*(1-(((ifnull(p.discount_rate,0))/100))),0) as fee
from truck t 
left join truck2 p on t.period =p.duration_type and t.car_type = p.car_type
where t.car_type='트럭'
order by fee desc, history_id desc