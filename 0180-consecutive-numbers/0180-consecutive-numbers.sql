# Write your MySQL query statement below
SELECT distinct num AS 'ConsecutiveNums'
FROM (
        SELECT num, LEAD(num) OVER() AS 'lead', LAG(num) OVER() AS 'lag'
        FROM Logs
    )t
WHERE t.num = t.lead AND t.num = t.lag