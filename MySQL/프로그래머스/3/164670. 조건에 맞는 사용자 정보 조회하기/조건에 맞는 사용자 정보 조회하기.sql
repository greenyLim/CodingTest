-- 코드를 입력하세요
SELECT u.user_id,u.nickname, 
concat(u.city,' ', u.street_address1,' ', u.Street_address2) as 전체주소,  
concat(substr(u.tlno,1,3),'-',substr(u.tlno,4,4),'-',substr(u.tlno,-4)) as 전화번호
from used_goods_board b
join used_goods_user u on b.writer_id=u.user_id
group by writer_id
having count(*)>=3
order by user_id desc