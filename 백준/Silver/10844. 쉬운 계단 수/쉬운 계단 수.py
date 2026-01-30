import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000

# dp[i][j] = 길이가 i이고 마지막 숫자가 j인 계단 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 길이 1: 1~9로 시작 가능 (0으로 시작 불가)
for j in range(1, 10):
    dp[1][j] = 1

# 길이 2부터 N까지
for i in range(2, N + 1):
    for j in range(10):
        if j > 0:  # 이전 숫자가 j-1
            dp[i][j] += dp[i-1][j-1]
        if j < 9:  # 이전 숫자가 j+1
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= MOD

# 길이 N인 계단 수의 총 개수
print(sum(dp[N]) % MOD)