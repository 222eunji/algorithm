def solution(array, n):
    cnt = 0
    for c in array:
        if c == n:
            cnt += 1
    return cnt