import sys
input = sys.stdin.readline

N = int(input())
dp = [100_0000] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    dp[i] = i # 줄일 수 없다면 1로만 이루어진게 최소 항의 수 
    for j in range(1, i):
        if j*j <= i:
            dp[i] = min(dp[i-j*j]+1, dp[i])
        else:
            break

print(dp[N])