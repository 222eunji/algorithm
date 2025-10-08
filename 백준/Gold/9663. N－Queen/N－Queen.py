import sys;
input = sys.stdin.readline

N = int(input())
col = [0] * (N+2)
rd_cross = [0] * (N*2)
ld_cross = [0] * (N*2)
ans = 0

def recur(row):
    global ans

    if row == N:
        ans += 1
        return
    for i in range(1, N+1):
        if col[i] == 1 or rd_cross[row-i+N] == 1 or ld_cross[row+i] == 1:
            continue
        col[i] = 1
        rd_cross[row-i+N] = 1
        ld_cross[row+i] = 1
        recur(row+1)
        col[i] = 0
        rd_cross[row-i+N] = 0
        ld_cross[row+i] = 0

recur(0)
print(ans)