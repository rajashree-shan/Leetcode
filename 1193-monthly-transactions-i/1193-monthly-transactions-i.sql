# Write your MySQL query statement below
select
DATE_FORMAT(trans_date,'%Y-%m') AS month,
country,
count(*) as trans_count,
SUM(CASE WHEN state = 'approved' then 1 ELSE 0 END) as approved_count,
SUM(CASE WHEN state = 'approved' then amount ELSE 0 END) AS approved_total_amount,
SUM(amount) as trans_total_amount
from Transactions
GROUP BY 
    DATE_FORMAT(trans_date, '%Y-%m'),
    country;