def solution(my_string):
    words = my_string.strip().split(" ")
    answer = []
    for ch in words:
        if ch:
            answer.append(ch)
    return answer