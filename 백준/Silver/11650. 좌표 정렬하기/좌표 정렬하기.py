import sys
input = sys.stdin.readline


N = int(input())

nums = [list(map(int, input().split())) for _ in range(N)]
nums.sort()

for x, y in nums:
    print(x, y)