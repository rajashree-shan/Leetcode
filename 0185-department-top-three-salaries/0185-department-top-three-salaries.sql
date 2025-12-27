# Write your MySQL query statement below
with temp as(
    select e.departmentId,e.name as Employee,e.Salary ,dense_rank() over (partition by e.departmentId order by e.salary desc) AS rnk
  FROM Employee e
)
select d.name as Department,t.Employee,t.salary as Salary from Temp t join Department d on t.departmentId=d.id where rnk<=3;