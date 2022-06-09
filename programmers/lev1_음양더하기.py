def solution(absolutes, signs):
    answer=0
    for absolute, sign in zip(absolutes, signs):
        if not sign:
            absolute *= (-1)
        answer+=absolute
    return answer


if __name__ == '__main__':
    input_list = [[4, 7, 12], [True, False, True], 9, [1, 2, 3], [False, False, True], 0]
    for input in input_list:
        print(input[2] == solution(input[0], input[1]))
