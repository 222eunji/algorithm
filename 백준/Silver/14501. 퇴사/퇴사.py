import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

memo = [-1] * N

def dp(i):
    if i >= N:
        return 0

    if memo[i] != -1:
        return memo[i]

    if i + lst[i][0] <= N:
        memo[i] = max(lst[i][1] + dp(i+lst[i][0]), dp(i+1)) # 상담을 진행하거나, 안하거나
    else:
        memo[i] = dp(i+1)

    return memo[i]

print(dp(0))
