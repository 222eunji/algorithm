-- 코드를 작성해주세요
SELECT route, CONCAT(ROUND(sum(d_between_dist),1), 'km') AS TOTAL_DISTANCE, CONCAT(ROUND(AVG(d_between_dist),2), 'km') AS AVERAGE_DISTANCE
FROM subway_distance
GROUP BY route
ORDER BY sum(d_between_dist) DESC