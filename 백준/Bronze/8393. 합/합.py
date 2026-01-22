import sys
input = sys.stdin.readline


x = int(input())
total = 0

for n in range(x+1):
    total += n

print(total)