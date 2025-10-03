import sys;
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(N):
    target = arr[i]
    l, r = 0, N-1
    while l < r:
        if l == i:  # 자기 자신은 제외
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        sum_v = arr[l] + arr[r]
        if sum_v == target:
            ans += 1
            break
        elif sum_v < target:
            l += 1
        else:
            r -= 1
print(ans)

