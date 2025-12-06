# Write your MySQL query statement below
select e.name,b.bonus from Employee e LEFT JOIN Bonus b on e.empId=b.empId WHERE b.bonus < 1000 OR b.bonus IS NULL;