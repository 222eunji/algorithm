def solution(start_num, end_num):
    answer = []
    n = start_num
    while n >= end_num:
        answer.append(n)
        n -= 1
    return answer