def solution(id_list, report, k):
    r_dict = {x: [0, False] for x in id_list}
    for r in list(set(report)):
        id, name = r.split(" ")
        r_dict[name][0] += 1
        if r_dict[name][0] >= k:
            r_dict[name][1] = True

    result_dict={x:0 for x in id_list}
    for rp in list(set(report)):
        id, name = rp.split(" ")
        if r_dict[name][1]:
            result_dict[id]+=1
    return list(result_dict.values())




if __name__ == '__main__':
    a = [["muzi", "frodo", "apeach", "neo"],
         ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2]
    b = [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3]
    c = [["con", "ryan", "frodo"], ["ryan frodo", "ryan con", "ryan con", "ryan con"], 1]

    d = [
        (a, [2, 1, 1, 0]),
        (b, [0, 0]),
        (c, [0, 2, 0])
    ]
    for x, y in d:
        # solution(x[0], x[1], x[2])
        print(y == solution(x[0], x[1], x[2]))
