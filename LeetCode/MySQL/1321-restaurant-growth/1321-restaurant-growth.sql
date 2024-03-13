# Write your MySQL query statement below
WITH sum_table AS (
    SELECT visited_on, SUM(amount) AS sum_amount
    FROM Customer
    GROUP BY visited_on
), 7sum_table AS (
    SELECT visited_on, SUM(sum_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS 7sum_amount
    FROM sum_table
), 7avg_table AS (
    SELECT visited_on, ROUND(AVG(sum_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS 7avg_amount
    FROM sum_table
)

SELECT S.visited_on, S.7sum_amount AS amount, A.7avg_amount AS average_amount
FROM 7sum_table AS S
JOIN 7avg_table AS A
ON S.visited_on = A.visited_on
WHERE S.visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM 7avg_table);