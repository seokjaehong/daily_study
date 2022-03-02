
# 입출력 예]
# no	new_id	result
# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	"z--"
# 예3	"=.="	"aaa"
# 예4	"123_.def"	"123_.def"
# 예5	"abcdefghijklmn.p"	"abcdefghijklmn"

if __name__ == '__main__':
    import re

    input_set = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    output_set = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]
    # input_set =["z-+.^."]
    # output_set= ["z--" ]

    def solution(new_id):
        d1 = new_id.lower()
        d2 = re.sub(r'[^0-9a-z-_.]', '', d1)
        d3 = re.sub(r'[..]{2,}', '.', d2)

        d4 = re.sub(r'^\.|\.$', '', d3)
        d5 = 'a' if len(d4) == 0 else d4
        d6_1 = d5[:15] if len(d5) >= 16 else d5
        d6_2 = re.sub(r'\.$', '', d6_1)
        d7 = d6_2
        if len(d6_2) <= 2:
            while len(d7) < 3:
                d7 += d6_2[-1]
        return d7


    for new_id in zip(input_set,output_set):

        answer = solution(new_id[0])
        print(answer== new_id[1])
