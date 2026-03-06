import sys
input = sys.stdin.readline

T = int(input())
dp = [1] * 101
for tc in range(T):
    N = int(input())
    if N >= 4:
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])