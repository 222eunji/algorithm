import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{tc}: {a} + {b} = {a+b}')