# Write your MySQL query statement below
WITH max_salary AS (
    SELECT DISTINCT MAX(salary) AS first
    FROM Employee
    ORDER BY salary DESC
)

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee, max_salary
WHERE salary < first;
