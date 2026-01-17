import sys
input = sys.stdin.readline

x = int(input())
result = 0

n = input().strip()
for c in n:
    result += int(c)

print(result)