from typing import List


def triangle(n) -> List[int]:
    result = [1] if n == 1 else [1] + list(map(sum, zip((p := triangle(n - 1))[:-1], p[1:]))) + [1]
    return result


def tri_result() -> int:
    n, k = map(int, input("줄의 번호와 칸의 번호를 공백을 한 칸 두고 입력하세요: ").split())
    result1 = triangle(n)
    return result1[k - 1]

def main():
    print(tri_result())


if __name__ == "__main__":
    main()
