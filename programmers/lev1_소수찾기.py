from itertools import combinations
def solution(nums):
    prime_list = []
    for x in range(2,sum(nums)+1):
        for y in range(2,x):
            if x%y ==0:
                break
        else:
            prime_list.append(x)
    sum_nums =[sum(x) for x in list(combinations(nums,3))]
    return sum([1 for x in sum_nums if x in prime_list])