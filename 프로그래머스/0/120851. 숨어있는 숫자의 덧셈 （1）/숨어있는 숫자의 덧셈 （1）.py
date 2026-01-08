def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isdigit():
            answer += int(c)
    return answer