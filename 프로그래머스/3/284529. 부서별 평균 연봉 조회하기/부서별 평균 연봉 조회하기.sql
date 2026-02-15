SELECT e.dept_id, d.dept_name_en, round(avg(e.sal),0) AS AVG_SAL
FROM hr_department d
JOIN hr_employees e ON d.dept_id = e.dept_id
GROUP BY e.dept_id
ORDER BY avg(e.sal) DESC