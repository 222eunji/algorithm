import sys;
input = sys.stdin.readline

N = int(input())
c = [False] * (N+1)
rd_cross = [False] * (2*N)
ld_cross = [False] * (2*N)
result = 0

def recur(row):
    global result
    if row == N:
        result += 1

    for col in range(1, N+1):
        if c[col] or rd_cross[col+row] or ld_cross[col-row+N-1]:
            continue
        c[col] = rd_cross[col+row] = ld_cross[col-row+N-1] = True
        recur(row+1)
        c[col] = rd_cross[col+row] = ld_cross[col-row+N-1] = False

recur(0)
print(result)