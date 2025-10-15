def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch not in 'aeiou':
            answer += ch
    return answer