SELECT animal_type, IFNULL(name, "No name"), sex_upon_intake
FROM animal_ins
ORDER BY animal_id;

# SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
# FROM ANIMAL_INS
# ORDER BY ANIMAL_ID;