# Write your MySQL query statement below
SELECT A.person_name
FROM Queue AS A
JOIN (SELECT person_id, SUM(weight) OVER(ORDER BY turn) AS Total_Weight
        FROM Queue) AS B
ON A.person_id = B.person_id
WHERE B.Total_Weight <= 1000
ORDER BY B.Total_Weight DESC
LIMIT 1;
