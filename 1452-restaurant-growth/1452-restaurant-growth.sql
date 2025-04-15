WITH DailyTotal AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
Rolling7Days AS (
    SELECT 
        dt1.visited_on,
        SUM(dt2.amount) AS total_amount,
        ROUND(SUM(dt2.amount) / 7, 2) AS average_amount
    FROM DailyTotal dt1
    JOIN DailyTotal dt2 
        ON dt2.visited_on BETWEEN DATE_SUB(dt1.visited_on, INTERVAL 6 DAY) AND dt1.visited_on
    GROUP BY dt1.visited_on
)
SELECT 
    visited_on, 
    total_amount AS amount, 
    average_amount
FROM Rolling7Days
WHERE visited_on >= (
    SELECT MIN(visited_on) FROM DailyTotal
) + INTERVAL 6 DAY
ORDER BY visited_on;
