def triangle_dp() -> int:
    n, k = map(int, input("줄의 번호와 칸의 번호를 공백을 한 칸 두고 입력하세요: ").split())
    pascal=[]
    for _ in (range(1, n + 1)):
        pascal = [[1], [1, 1]]
        for i in range(2, n):
            new = [1]
            for j in range(i - 1):
                new += [pascal[i - 1][j] + pascal[i - 1][j + 1]]
            new += [1]
            pascal += [new]
    return pascal[n-1][k-1]
    # edit here

    #################


def main():
    print(triangle_dp())


if __name__ == "__main__":
    main()
