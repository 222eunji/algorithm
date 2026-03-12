-- 코드를 작성해주세요
SELECT id, fish_name, length
FROM fish_info i JOIN fish_name_info n ON i.fish_type = n.fish_type
WHERE (i.fish_type, i.length) IN (
    SELECT fish_type, max(length)
    FROM fish_info
    GROUP BY fish_type
)
ORDER BY id

# 종류별로 가장 큰 물고기
# ID(ID), 물고기 이름(FISH_NAME), 길이(LENGTH) 출력
# 물고기의 ID에 대해 오름차순 정렬
