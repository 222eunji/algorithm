def solution(num_list):
    mulv = 1
    sumv = 0
    for n in num_list:
        mulv *= n
        sumv += n
    sumv = sumv*sumv
    if mulv < sumv:
        return 1
    return 0