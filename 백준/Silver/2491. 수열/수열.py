N = int(input())
arr = list(map(int, input().split()))

max_len = 1
cnt_up = 1
cnt_down = 1
for i in range(1, len(arr)):
    # 증가 하는 경우
    if arr[i-1] <= arr[i]:
        cnt_up += 1
    else:
        if max_len <= cnt_up:
            max_len = cnt_up
        cnt_up = 1

    # 감소 하는 경우
    if arr[i-1] >= arr[i]:
        cnt_down += 1
    else:
        if max_len <= cnt_down:
            max_len = cnt_down
        cnt_down = 1

max_len = max(max_len, cnt_up, cnt_down)
print(max_len)