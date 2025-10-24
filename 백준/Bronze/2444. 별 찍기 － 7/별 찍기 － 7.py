import sys
input = sys.stdin.readline

N = int(input())

for n in range(1, N):
    print(' '*(N-n-1), '*'*(2*n-1))
print('*'*(2*N-1))
for n in range(N-1, 0, -1):
    print(' '*(N-n-1), '*'*(2*n-1))