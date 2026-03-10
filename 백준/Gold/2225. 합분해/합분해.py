import sys
 
input = sys.stdin.readline
 
n,k = map(int,input().split())
mod = 1000000000
d=[[0]*(k+1) for _ in range(n+1)]
 
for i in range(n+1):
    for j in range(1,k+1):
        if i==0:
            d[i][j]=1
        else:
            d[i][j] = (d[i-1][j]+d[i][j-1])%mod
print(d[-1][-1])
