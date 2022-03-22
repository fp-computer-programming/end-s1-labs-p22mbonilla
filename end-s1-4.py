# Author MB 03/21/2022

def solution(nums):
    if not nums:
        return []
    return sorted(nums)

print(solution([1,2,3,4,5]) == [1,2,3,5])
print(solution([25,2,10]) == [2,10,25])