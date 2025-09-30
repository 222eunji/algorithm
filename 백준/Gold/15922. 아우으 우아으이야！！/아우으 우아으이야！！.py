import sys;
input = sys.stdin.readline

N = int(input())
# 초기값 설정
x0, y0 = map(int, input().split())
length = 0
for _ in range(N-1):
    x, y = map(int, input().split())
    if x <= y0 and y >= y0:
        y0 = y
    elif x > y0:
        length += (y0-x0) # 길이 더해주고
        x0, y0 = x, y   # 초기화
length += (y0-x0)   # 마지막 값 더해주기
print(length)