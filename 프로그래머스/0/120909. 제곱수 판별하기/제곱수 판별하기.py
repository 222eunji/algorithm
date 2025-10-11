def solution(n):
    for num in range(1, n//2+1):
        if num*num == n:
            return 1
    return 2