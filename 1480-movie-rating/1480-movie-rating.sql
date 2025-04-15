# Write your MySQL query statement below
# Write your MySQL query statement below
(SELECT name as results
FROM Users U JOIN MovieRating R ON U.user_id = R.user_id
GROUP BY U.user_id
ORDER BY Count(*) DESC, name
LIMIT 1)
UNION ALL
(SELECT m.title as results
FROM Movies m Right JOIN MovieRating R ON m.movie_id = R.movie_id
WHERE R.created_at BETWEEN '2020-02-01' AND '2020-02-28'
GROUP BY m.movie_id
ORDER BY avg(rating) DESC, m.title
LIMIT 1)