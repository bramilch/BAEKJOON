# Write your MySQL query statement below
SELECT S.user_id, ROUND(SUM(IF(C.action = 'confirmed', 1, 0)) / COUNT(*), 2) AS confirmation_rate
FROM Signups AS S
LEFT JOIN Confirmations AS C
ON S.user_id = C.user_id
GROUP BY s.user_id;