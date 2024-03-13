# Write your MySQL query statement below
WITH latlon_value AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(pid) = 1
), tiv2015_value AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) != 1
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE (lat, lon) IN (SELECT * FROM latlon_value) AND tiv_2015 IN (SELECT * FROM tiv2015_value);

# Right Answer2
-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM Insurance
-- WHERE tiv_2015 IN (
--     SELECT tiv_2015
--     FROM Insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(tiv_2015) > 1
-- ) AND (lat, lon) IN (
--     SELECT lat, lon
--     FROM Insurance
--     GROUP BY lat, lon
--     HAVING COUNT(*) = 1
-- );

# Wrong answer1
-- WITH remove_duplicate AS (
--     SELECT pid, tiv_2015, tiv_2016
--     FROM Insurance
--     GROUP BY lat, lon
--     HAVING COUNT(pid) = 1
-- ), same_tiv2015 AS (
--     SELECT pid, COUNT(tiv_2015) OVER (PARTITION BY tiv_2015) AS num_tiv2015, tiv_2016 # 비효율적
--     FROM remove_duplicate # 앞에서 만들어준 테이블에서 tiv_2015가 1개 이상인 pid, tiv_2016 추출
-- )

-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM same_tiv2015
-- WHERE num_tiv2015 >= 2;

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
-- WHERE tiv_2015 IN more_tiv2015 AND (lat, lon) IN lat_lon; # 테이블 이름으로 넣어주면 안 되고 Subquery로 넣어줘야 한다.

