if __name__ == '__main__':
    # s_list = ["one4seveneight"]
    s_list = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    result_list = [
        1478,
        234567,
        234567,
        123]


    def solution(s):
        answer = ""
        dic = {
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        tmp = ""
        for m in s:
            tmp += str(m)
            if tmp in dic.keys():
                answer += str(dic[tmp])
                tmp = ""
            if tmp in dic.values():
                answer += str(tmp)
                tmp = ""
        return int(answer)


    # def solution(s):
    #     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #
    #     for i in range(len(words)):
    #         s = s.replace(words[i], str(i))
    #
    #     return int(s)

    for s in zip(s_list, result_list):
        a = solution(s[0])
        assert a == s[1]