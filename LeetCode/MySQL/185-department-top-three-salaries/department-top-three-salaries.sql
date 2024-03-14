# Write your MySQL query statement below
WITH temp01 AS (
    SELECT D.name AS Department, E.name AS Employee,
        DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS tmp, E.salary AS Salary
    FROM Employee AS E
    JOIN Department AS D
    ON E.departmentId = D.id
)

SELECT Department, Employee, Salary
FROM temp01
WHERE tmp < 4;
