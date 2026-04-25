def solution(my_string):
    answer = [c for c in my_string.lower()]
    answer.sort()

    return ''.join(answer)