from itertools import combinations
def solution(nums):
    nums_list = list(set(nums))
    cnt = int(len(nums)/2)
    nums_cnt = len(nums_list)
    return nums_cnt if nums_cnt<cnt else cnt
    # return min(len(ls) / 2, len(set(ls)))


if __name__ == '__main__':
    input_list = [
        ([3, 1, 2, 3], 2),
        ([3, 3, 3, 2, 2, 4], 3),
        ([3, 3, 3, 2, 2, 2], 2),
        ([1, 2, 3, 4, 5, 6], 3),
    ]
    for input in input_list:
        print(input[1] == solution(input[0]))
