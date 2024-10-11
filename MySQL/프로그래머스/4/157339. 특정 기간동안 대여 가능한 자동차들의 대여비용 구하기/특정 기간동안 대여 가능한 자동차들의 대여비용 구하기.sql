-- 코드를 입력하세요
SELECT C.CAR_ID, NP.CAR_TYPE, 
round((daily_fee * 30 * (100 - CAST(replace(discount_rate, '%', '') AS unsigned))) / 100,0)  AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
         JOIN (SELECT car_id,
                      COUNT(
                              CASE
                                  WHEN start_date > '2022-11-30' 
                          OR end_date <'2022-11-01'
                                      THEN NULL
                                  ELSE 1
                                  END) AS temp
               FROM car_rental_company_rental_history
               GROUP BY car_id
               HAVING temp = 0) N 
               ON C.car_id = N.car_id
         JOIN (SELECT *
               FROM car_rental_company_discount_plan P
               WHERE DURATION_TYPE LIKE '30%') NP
               ON C.CAR_TYPE=NP.CAR_TYPE
               
WHERE NP.CAR_TYPE='SUV' OR  NP.CAR_TYPE='세단'
having 500000 <= FEE AND  FEE <= 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC