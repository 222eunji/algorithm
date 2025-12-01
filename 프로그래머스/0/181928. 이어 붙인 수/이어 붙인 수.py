def solution(num_list):
    even_num = ''
    odd_num = ''
    
    for n in num_list:
        if n % 2 == 0:
            even_num += str(n)
        else:
            odd_num += str(n)

    return int(even_num) + int(odd_num)