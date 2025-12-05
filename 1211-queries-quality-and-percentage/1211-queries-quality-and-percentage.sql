# Write your MySQL query statement below
select query_name ,
ROUND(AVG(rating * 1.0/position),2) as quality,
ROUND(AVG(CASE WHEN RATING <3 THEN 1.0 else 0.0 END)*100,2) as poor_query_percentage from Queries
group by query_name;