-- 코드를 작성해주세요
SELECT count(ID) as FISH_COUNT, max(IFNULL(LENGTH,10)) as MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
group by fish_type
having avg(IFNULL(LENGTH,10)) >= 33
order by fish_type
