import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# dp = list([0] * K for _ in range(N + 1))
dp = [[0] * (N+1) for _ in range(K + 1)]

# 1개로 N 만들기
for i in range(N+1):
    dp[1][i] = 1

# K개로 N 만들기
for k in range(2, K+1):
    for i in range(0, N+1):
        for j in range(0, i+1):
            dp[k][i] += dp[k-1][j]
# print(dp)
print(dp[K][N] % 1000000000)