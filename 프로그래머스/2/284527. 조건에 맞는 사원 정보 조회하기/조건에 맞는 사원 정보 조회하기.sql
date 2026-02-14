SELECT sum(g.score) AS "SCORE", g.emp_no, e.emp_name, e.position, e.email
FROM hr_department d
JOIN hr_employees e ON d.DEPT_ID = e.DEPT_ID
JOIN hr_grade g ON e.EMP_NO = g.EMP_NO
GROUP BY g.EMP_NO
ORDER BY 1 DESC LIMIT 1