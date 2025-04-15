WITH RankedEmployees AS (
    SELECT 
        e.id,
        e.name AS Employee,
        e.salary,
        d.name AS Department,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT 
    Department,
    Employee,
    salary AS Salary
FROM RankedEmployees
WHERE rnk <= 3;
