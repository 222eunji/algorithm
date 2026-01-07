def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    
    temp = [1, 2, 3]
    new = temp + [0] * 2
    print([0] * 5)
    print(new)
    
    if row_len == col_len:
        return arr
    elif row_len > col_len:
        add_arr = [0] * (row_len-col_len)
        for i in range(row_len):
            arr[i] += add_arr
    else:
        add_arr = [0] * col_len
        for _ in range(col_len-row_len):
            arr.append(add_arr)
    return arr