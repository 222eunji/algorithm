SELECT count(*) AS FISH_COUNT
FROM fish_info i JOIN fish_name_info n ON i.fish_type = n.fish_type
WHERE n.fish_name IN ('BASS', 'SNAPPER')

# FISH_INFO 테이블에서 잡은 BASS와 SNAPPER의 수를 출력하는 SQL 문을 작성해주세요.
# 컬럼명은 'FISH_COUNT`로 해주세요.