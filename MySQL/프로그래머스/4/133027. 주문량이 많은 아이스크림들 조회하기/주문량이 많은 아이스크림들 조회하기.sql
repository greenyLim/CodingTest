-- 코드를 입력하세요
SELECT b.flavor
from first_half a
right join july b
on a.flavor = b.flavor and a.shipment_id=b.shipment_id

group by b.flavor
order by a.total_order+sum(b.total_order) desc
limit 3