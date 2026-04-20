
def min_max(N, arr):
    min_v = arr[0]
    max_v = arr[0]

    for i in range(1, N):
        if min_v > arr[i]:
            min_v = arr[i]
        elif max_v < arr[i]:
            max_v = arr[i]
    
    return max_v - min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {min_max(N, arr)}')