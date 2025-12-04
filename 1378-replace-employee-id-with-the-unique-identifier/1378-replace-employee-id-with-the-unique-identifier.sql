# Write your MySQL query statement below
SELECT Emu.unique_id, E.name
FROM Employees E
LEFT JOIN EmployeeUNI Emu
ON E.id = Emu.id;
