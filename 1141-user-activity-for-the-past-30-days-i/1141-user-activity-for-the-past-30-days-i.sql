# Write your MySQL query statement below
select activity_date as day,count(DISTINCT user_id)as active_users from Activity where DATEDIFF("2019-07-27",activity_date) BETWEEN 0 AND 29
GROUP BY activity_date;
