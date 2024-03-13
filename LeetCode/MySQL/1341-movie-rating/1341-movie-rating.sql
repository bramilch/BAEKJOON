# Write your MySQL query statement below
WITH greatest_user AS (
    SELECT U.name AS name
    FROM MovieRating AS M
    JOIN Users AS U
    ON M.user_id = U.user_id
    GROUP BY M.user_id
    HAVING COUNT(M.user_id)
    ORDER BY COUNT(M.user_id) DESC, U.name
    LIMIT 1
), highest_movie AS(
    SELECT M.title AS title
    FROM MovieRating AS R
    JOIN Movies AS M
    ON R.movie_id = M.movie_id
    WHERE YEAR(R.created_at) = 2020 AND MONTH(R.created_at) = 2
    GROUP BY R.movie_id
    HAVING AVG(R.rating)
    ORDER BY AVG(R.rating) DESC, M.title
    LIMIT 1
)

SELECT name AS results
FROM greatest_user
UNION ALL
SELECT title
FROM highest_movie;