import array

arr = array.array('i',[99, 0, -7, 0, 16])   # 키워드 'i'는 integer, 'f'면 float
# for i in range(len(arr)):
#     print(f"{arr[i]:2} {id(arr[i])}")

def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list

arr = move_zeros(arr)
print(arr)