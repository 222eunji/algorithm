def solution(array):
    array.sort()
    i = len(array) // 2
    answer = array[i]
    return answer