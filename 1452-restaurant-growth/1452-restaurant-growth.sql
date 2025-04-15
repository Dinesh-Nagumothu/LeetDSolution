# Write your MySQL query statement below
WITH daily_amount AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
sum_amt AS (
    SELECT visited_on, 
        SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM daily_amount
)
SELECT visited_on, amount, average_amount
FROM sum_amt
WHERE visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM daily_amount), INTERVAL 6 DAY)
ORDER BY visited_on;