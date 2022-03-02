if __name__ == '__main__':
    def solution(n):
        answer = []
        r = 0
        while n > 0:
            n, mod = divmod(n, 3)
            answer.append(mod)

        for i in range(len(answer)):
            r += answer[i] * 3 ** (len(answer) - i - 1)
        return r


    n = [45, 125]
    result = [7, 229]

    for num, r in zip(n, result):
        answer = solution(num)
        assert answer == r
