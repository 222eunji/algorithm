def solution(n):
    answer = 0
    cur = 6

    while cur % n != 0:
        cur += 6

    answer = cur // 6

    return answer