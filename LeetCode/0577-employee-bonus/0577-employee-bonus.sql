# Write your MySQL query statement below
SELECT E.name, B.bonus
FROM Employee AS E
LEFT JOIN Bonus AS B
ON B.empId = E.empId
WHERE B.bonus < 1000 OR B.bonus is NULL;
-- UNION
-- SELECT *
-- FROM Employee AS E
-- RIGHT JOIN Bonus AS B
-- ON B.empId = E.empId
