def solution(arr):
    q = []
    q.append(arr[0])
    for n in arr:
        if q[-1] == n:
            pass
        else:
            q.append(n)
    return q