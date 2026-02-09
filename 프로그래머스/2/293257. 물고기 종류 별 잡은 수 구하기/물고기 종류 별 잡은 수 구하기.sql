SELECT count(*) AS FISH_COUNT, FISH_NAME
FROM fish_info i
JOIN fish_name_info n
    ON i.FISH_TYPE = n.FISH_TYPE
GROUP BY fish_name
ORDER BY 1 desc