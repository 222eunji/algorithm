import sys;
input = sys.stdin.readline

row = []
col = []

total_c, total_r = map(int, input().split())
n = int(input())
for _ in range(n):
    sign, num = map(int, input().split())
    if sign == 1:
        col.append(num)
    else:
        row.append(num)

row.sort()
col.sort()
row.append(total_r)
col.append(total_c)

pre_r = 0
pre_c = 0
max_size = -1

for now_r in row:
    for now_c in col:
        size = (now_r-pre_r) * (now_c-pre_c)
        max_size = max(max_size, size)
        pre_c = now_c
    pre_c = 0
    pre_r = now_r
    
print(max_size)