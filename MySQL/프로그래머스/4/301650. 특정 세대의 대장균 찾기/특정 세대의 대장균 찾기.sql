with second as (select a.id as id, b.id as parent_id
              from ecoli_data a 
              left join ecoli_data b on a.parent_id=b.id
              where a.parent_id is not null
              order by parent_id),
    third as (select a.id as id, b.id as parent_id
             from second a
             left join second b on a.parent_id=b.id
             where a.parent_id is not null)
             
select a.id as id
from third a
left join third b on a.parent_id=b.id
where (b.id is not null) and (b.parent_id is null)
order by id