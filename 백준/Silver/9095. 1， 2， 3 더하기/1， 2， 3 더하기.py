import sys
input = sys.stdin.readline

T = int(input())

numbers = []
for _ in range(T):
    numbers.append(int(input()))

dp = [0] * (max(numbers) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, (max(numbers) + 1)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in numbers:
    print(dp[n])