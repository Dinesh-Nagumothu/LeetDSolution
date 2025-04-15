/* Write your T-SQL query statement below */
WITH unique_location AS(
    SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(pid) = 1
),
all_valid_tiv2015 AS(
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(pid) > 1
)

SELECT ROUND(SUM(tiv_2016 * 1.0), 2) AS tiv_2016
FROM Insurance i
WHERE EXISTS (
    SELECT 1 FROM unique_location ul 
    WHERE i.lat = ul.lat AND i.lon = ul.lon
)
AND tiv_2015 IN (SELECT tiv_2015 FROM all_valid_tiv2015);