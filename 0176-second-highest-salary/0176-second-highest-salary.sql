SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)

# SELECT IFNULL(
#        (SELECT DISTINCT Salary 
#         FROM Employee
#         ORDER BY salary DESC 
#         LIMIT 1 OFFSET 1),
#         NULL) AS SecondHighestSalary
        
