def solution(a, b):
    a, b = str(a), str(b)
    x, y = a+b, b+a
    x, y = int(x), int(y)
    answer = max(x, y)
    return answer