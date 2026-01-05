def solution(s):
    lst = s.split()
    lst_int = [ int(v) for v in lst]

    min_v = min(lst_int)
    max_v = max(lst_int)
    
    print(min_v)
    print(max_v)
    answer = f'{min_v} {max_v}'
    return answer