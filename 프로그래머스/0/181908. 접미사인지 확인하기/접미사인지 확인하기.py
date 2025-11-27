def solution(my_string, is_suffix):
    if is_suffix in my_string:
        for i in range(len(my_string)):
            if my_string[i:] == is_suffix:
                return 1
    return 0