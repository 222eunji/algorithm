def solution(my_strings, parts):
    answer = []
    for i in range(len(parts)):
        my_string, part = my_strings[i], parts[i]
        s, e = part[0], part[1]
        answer.append(my_string[s:e+1])
    result = "".join(answer)
    
    return result