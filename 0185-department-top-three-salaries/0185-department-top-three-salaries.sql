/* Write your T-SQL query statement below */
SELECT Department, Employee, Salary
FROM(
    SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS d_rank
    FROM Employee E INNER JOIN Department D ON E.departmentId = D.id
) T
WHERE d_rank <= 3;