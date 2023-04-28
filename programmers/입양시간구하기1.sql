-- 코드를 입력하세요
SELECT date_format(datetime, '%H') as Hour, count(*)
from animal_outs
group by Hour
having Hour between 9 and 21
order by Hour asc