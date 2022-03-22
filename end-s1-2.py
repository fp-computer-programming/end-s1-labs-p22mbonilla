# Author MB 03/21/2022

def double_every_other(lst):
    if type(lst) == list:
        for i,v in enumerate(lst):
            if not i % 2== 0:
                lst[i]= v * 2
    return lst

print(double_every_other([1,2,3,4,5]) == [1,4,3,8,5])