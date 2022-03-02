def solution(id_list, report, k):
    report_dict = {x: 0 for x in id_list}
    user_dict = {x: list() for x in id_list}
    ck_list = []
    for r in report:
        kk, v = r.split(" ")
        if r in ck_list:
            report_dict[v] = 1
            user_dict[kk] = [v]
        else:
            report_dict[v] += 1
            user_dict[kk] += [v]
        ck_list.append(r)

    stop_id_dict = dict(filter(lambda elem: elem[1] >= k, report_dict.items()))

    result = {x: 0 for x in id_list}
    for u_k, u_v in user_dict.items():
        for s_k, s_v in stop_id_dict.items():
            if s_k in u_v:
                result[u_k] += 1
    answer = list(result.values())
    return answer

    # print(stop_id_list)
    # result = {x: list() for x in id_list}
    # for r in report:
    #     a, b = r.split(" ")
    #     if b in stop_id_list:
    #         result[a] += [b]
    # answer = [len(v) for k, v in result.items()]
    # answer=[]
    # return answer


if __name__ == '__main__':
    a = [["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2]
    b = [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3]
    c = [["con", "ryan", "frodo"], ["ryan frodo", "ryan con", "ryan con", "ryan con"], 1]

    d = [
        (a, [2, 1, 1, 0]),
        (b, [0, 0]),
        (c, [0, 2, 0])
    ]
    for x, y in d:
        print(y == solution(x[0], x[1], x[2]))
