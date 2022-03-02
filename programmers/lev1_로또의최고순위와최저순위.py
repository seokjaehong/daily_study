if __name__ == '__main__':
    input_lotto_list = [
        [44, 1, 0, 0, 31, 25],
        [0, 0, 0, 0, 0, 0],
        [45, 4, 35, 20, 3, 9]
    ]
    win_nums_list = [
        [31, 10, 45, 1, 6, 19],
        [38, 19, 20, 40, 15, 25],
        [20, 9, 3, 45, 4, 35]]

    result_list = [
        [3, 5],
        [1, 6],
        [1, 1]
    ]


    def solution(lottos, win_nums):
        min_num = len(set(lottos) & set(win_nums))
        zero_cnt = lottos.count(0)

        answer = [get_ranking(min_num + zero_cnt), get_ranking(min_num)]
        return answer


    def get_ranking(k):
        if k == 6:
            return 1
        elif k == 5:
            return 2
        elif k == 4:
            return 3
        elif k == 3:
            return 4
        elif k == 2:
            return 5
        else:
            return 6


    cnt = 1
    for i, w, r in zip(input_lotto_list, win_nums_list, result_list):
        print("#", cnt)
        a = solution(i, w)
        print(a)

        cnt += 1
