# Write your MySQL query statement below
WITH all_id AS (
    SELECT requester_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id
    FROM RequestAccepted
    )

SELECT requester_id AS id, COUNT(requester_id) AS num
FROM all_id
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1;