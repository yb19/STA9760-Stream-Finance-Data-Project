select a.*, b.ts
from
(
select name, substr(ts, 12, 2) as hour, max(high) as highest
from "stream-finance-db"."19"
group by name, substr(ts, 12, 2)
) a
join 
(
select name, ts, substr(ts, 12, 2) as hour, high
from "stream-finance-db"."19"
) b
on a.name = b.name and a.hour = b.hour and a.highest = b.high
order by a.name, a.hour;}