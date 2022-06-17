def solution(numbers):
    return sum(set([x for x in range(1, 10)]).difference(set(numbers)))


if __name__ == '__main__':
    input_list = [
        [[1, 2, 3, 4, 6, 7, 8, 0], 14],
        [[5, 8, 4, 0, 6, 7, 9], 6]
    ]
    for input in input_list:
        print(input[1] == solution(input[0]))
