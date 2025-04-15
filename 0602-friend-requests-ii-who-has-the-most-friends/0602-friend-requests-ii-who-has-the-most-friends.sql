# Write your MySQL query statement below
select t1.id as id, count(*) as num from (SELECT requester_id AS id FROM requestaccepted
UNION ALL 
SELECT accepter_id AS id FROM requestaccepted) t1 
group by id order by num DESC limit 1;

