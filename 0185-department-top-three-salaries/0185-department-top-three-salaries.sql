# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS result
        FROM Employee e
        JOIN Department d
        ON e.departmentId = d.id
     ) r WHERE r.result <= 3

