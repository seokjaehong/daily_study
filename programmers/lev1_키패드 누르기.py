def get_distance(a, b):
    d = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return d


def solution(numbers, hand):
    answers = ""
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    left_curr, right_curr = [3, 0], [3, 2]

    for number in numbers:
        num_index = [0, 0]
        for i, el in enumerate(keypad):
            if number in el:
                num_index = [i, el.index(number)]
                break
        # print(num_index)
        if number in [1, 4, 7]:
            answers += "L"
            left_curr = num_index
        elif number in [3, 6, 9]:
            answers += "R"
            right_curr = num_index
        else:
            if get_distance(left_curr, num_index) < get_distance(right_curr, num_index):
                answers += "L"
                left_curr = num_index
            elif get_distance(left_curr, num_index) > get_distance(right_curr, num_index):
                answers += "R"
                right_curr = num_index
            else:
                if hand == 'right':
                    answers += "R"
                    right_curr = num_index
                else:
                    answers += "L"
                    left_curr = num_index
    return answers


if __name__ == '__main__':
    # t1 = [[1, 3, 4], 'right', 'LRL']
    t1 = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"]
    t2 = [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"]
    t3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL"]
    # t_list = [t2]
    t_list = [t1, t2, t3]
    for t in t_list:
        # print(t2)
        # print(solution(t[0], t[1]))
        print(t[2] == solution(t[0], t[1]))
