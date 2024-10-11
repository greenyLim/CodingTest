-- 코드를 입력하세요
SELECT a.member_name, b.review_text, 
    DATE_FORMAT(b.review_date, '%Y-%m-%d') AS review_date
FROM member_profile a
right join rest_review b
on a.member_id = b. member_id
where b.member_id = (select member_id
                  from rest_review
                  group by member_id
                  order by count(*) desc
                  limit 1)
order by review_date, review_text
