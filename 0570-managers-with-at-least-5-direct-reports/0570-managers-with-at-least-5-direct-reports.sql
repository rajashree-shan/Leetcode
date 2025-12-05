# Write your MySQL query statement below
select a.name from Employee a JOIN employee b on a.id=b.managerId group by b.managerID having count(b.id)>=5;