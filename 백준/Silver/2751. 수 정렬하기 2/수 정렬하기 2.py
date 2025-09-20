import sys;
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort()
for i in range(N):
    print(arr[i])