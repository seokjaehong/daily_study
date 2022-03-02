import math

dots = [[(1.0, 1.0), (1.0, -1.0), (-1.0, -1.0), (-1.0, 1.0)],
        [(0.0, 2.0), (1.0, 0.0), (-1.0, 0.0)]]


def getDistance(tuple1, tuple2) -> float:
    ### edit here

    # get distance between two dots

    #################
    a = abs(tuple1[0] - tuple2[0])
    b = abs(tuple1[1] - tuple2[1])
    distance = math.sqrt(a * a + b * b)
    return distance


def calcRectangleArea(t) -> float:
    ### edit here

    # get width
    # get height  
    # get area 

    #################

    # # * 이때 사각형은 직사각형 혹은 정사각형만 주어진다.
    width = getDistance(t[0], t[1])
    height = getDistance(t[1], t[2])
    area = width * height

    # Brahmagupta's formula
    # a = getDistance(t[0], t[1])
    # b = getDistance(t[1], t[2])
    # c = getDistance(t[2], t[3])
    # d = getDistance(t[3], t[0])
    # s = (a + b + c + d) / 2
    # area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

    return area


def calcTriangleArea(t) -> float:
    ### edit here

    # get distance of side a 
    # get distance of side b
    # get distance of side c
    # get s 
    # get area

    #################
    # * 삼각형의 넓이를 구할 때는 헤론의 공식을 사용한다
    a = getDistance(t[0], t[1])
    b = getDistance(t[1], t[2])
    c = getDistance(t[2], t[0])

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


def main():
    area = 0
    for i in dots:
        print(i)
        if len(i) == 3:
            print('면적:', calcTriangleArea(i))
        elif len(i) == 4:
            print('면적:', calcRectangleArea(i))
        else:
            pass


if __name__ == "__main__":
    # 좌표평면 위 두 점 사이 거리를 이용해 삼각형과 사각형의 넓이를 구한다.

    main()
