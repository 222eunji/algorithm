
N, M = map(int, input().split())
arr = list(range(1, N+1))

temp = []
def perm(arr):
    if len(temp) == M:
        print(*temp)
    for i in range(N):
        if arr[i] in temp:
            continue
        temp.append(arr[i])
        perm(arr)
        temp.pop()

perm(arr)