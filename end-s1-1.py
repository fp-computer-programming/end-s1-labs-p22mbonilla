# Author MB 03/21/2022

def move_zeros(array):
    n = 0
    for i in range(len(array)):
        if array[i-n] == 0:
            array.pop(i-n)
            array.append(0)
            n += 1
    return array

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))