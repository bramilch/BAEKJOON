# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) > 1
) AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);

# Wrong answer2
-- WITH more_tiv2015 AS (
--     SELECT tiv_2015
--     FROM Insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(tiv_2015) > 1
-- ), lat_lon AS (
--     SELECT lat, lon
--     FROM Insurance
--     GROUP BY lat, lon
--     HAVING COUNT(*) = 1
-- )

-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM Insurance
-- WHERE tiv_2015 IN more_tiv2015 AND (lat, lon) IN lat_lon;

# Wrong answer1
-- WITH remove_duplicate AS (
--     SELECT pid, tiv_2015, tiv_2016
--     FROM Insurance
--     GROUP BY lat, lon
--     HAVING COUNT(pid) = 1
-- ), same_tiv2015 AS (
--     SELECT pid, COUNT(tiv_2015) OVER (PARTITION BY tiv_2015) AS num_tiv2015, tiv_2016
--     FROM remove_duplicate
-- )

-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM same_tiv2015
-- WHERE num_tiv2015 >= 2;