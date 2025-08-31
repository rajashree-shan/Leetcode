/* Write your PL/SQL query statement below */
select name as Customers from customers  where id not in (select customerId from Orders);