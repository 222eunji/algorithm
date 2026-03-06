import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = 1

if n >= 2:
    dp[2] = 3

for i in range(3, n+1):
    if i % 2:   # 홀수
        pass
    else:       # 짝수
        dp[i] = 3*dp[i-2]
        for j in range(4, i+1, 2):
            dp[i] += 2*dp[i-j]

print(dp[n])