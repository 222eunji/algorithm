def solution(box, n):
    answer = 1
    for line in box:
        answer *= line // n
    return answer