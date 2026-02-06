import sys
input = sys.stdin.readline

# 이친수
# 0으로 시작하지 않고
# 1이 두번 연속으로 나타나지 않는다

N = int(input())
# [0으로 끝나는수, 1로 끝나는수]
dp = list([0,0] for _ in range(N+1))
dp[1][1] = 1

for i in range(2, N+1):
    for j in range(2):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

print(sum(dp[N]))