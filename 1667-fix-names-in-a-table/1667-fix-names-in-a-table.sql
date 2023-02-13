# Write your MySQL query statement below
SELECT 
    user_id,
    CONCAT(UPPER(SUBSTR(u.name,1,1)),LOWER(SUBSTR(name,2))) AS name
FROM Users u
ORDER BY u.user_id