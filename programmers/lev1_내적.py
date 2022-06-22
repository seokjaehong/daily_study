def solution(a, b):
    answer = sum([x*y for x,y in zip(a,b)])
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 4],[-3, -1, 0, 2])==3)

