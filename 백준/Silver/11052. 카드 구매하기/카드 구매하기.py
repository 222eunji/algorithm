import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst = [0] + lst
l = len(lst)

dp = [0] * (N+1)

for i in range(1, N+1):
    for idx in range(1, l+1):
        if i-idx < 0:
           break
        dp[i] = max(dp[i], dp[i-idx] + lst[idx])

print(dp[N])
    