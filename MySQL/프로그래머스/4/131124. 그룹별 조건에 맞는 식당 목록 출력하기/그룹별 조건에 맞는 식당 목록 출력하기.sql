with member_group as (select *, count(*) as count_review
                      from rest_review
                      group by member_id
                      order by count_review desc
                     limit 1)

select m.member_name, r.review_text, date_format(r.review_date,'%Y-%m-%d') as review_date
from member_profile m
left join rest_review r on m.member_id=r.member_id
where m.member_id in (select member_id
                     from member_group)
order by review_date, review_text
