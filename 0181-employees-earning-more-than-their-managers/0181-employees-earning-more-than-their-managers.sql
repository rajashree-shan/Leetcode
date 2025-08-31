# Write your MySQL query statement below
select E.name as Employee from Employee E JOIN Employee M on E.managerId=M.id and E.salary > M.salary;