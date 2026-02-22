import sys
input = sys.stdin.readline

n = int(input())
wine = list(int(input()) for _ in range(n))

dp = [[0,0,0] for _ in range(n)]
# 안 마셨을 경우, 한번 쉬고 마셨을 경우, 두번 연속 마셨을 경우
dp[0][0], dp[0][1] = 0, wine[0]

for i in range(1, n):
    # 안마실 경우
    dp[i][0] = max(dp[i-1])
    # 한번쉬고 마실 경우
    dp[i][1] = dp[i-1][0] + wine[i]
    # 연속으로 마실 경우
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n-1]))