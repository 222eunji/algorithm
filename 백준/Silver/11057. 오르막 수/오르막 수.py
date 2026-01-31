import sys
input = sys.stdin.readline

# 1. 한자릿 수는 10개만 가능
# 2. 마지막 자리 보다 같거나 큰수 만큼 더해짐
N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N]) % 10_007)
