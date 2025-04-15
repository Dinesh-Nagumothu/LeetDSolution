SELECT Department,Employee,Salary FROM(SELECT D.id,D.name AS   Department,C.name as Employee,DENSE_RANK() OVER(partition by C.departmentId order by C.salary desc ) as rnk,C.salary from Department D join Employee C on D.id=C.departmentid) tmp
where
rnk<=3