import numpy as np
from typing import List


def check_board() -> List[int]:
    ### edit here

    #################
    arr = np.full((10, 10), 0)
    cnt_x = 0
    for x in arr:
        if cnt_x == 0 or cnt_x == 9:
            arr[cnt_x] = [2] * 10
        else:
            cnt_y = 0
            for _ in x:
                if cnt_y == 0 or cnt_y == 9:
                    arr[cnt_x][cnt_y] = 2
                else:
                    arr[cnt_x][cnt_y] = (cnt_x + cnt_y) % 2
                cnt_y += 1
        cnt_x += 1
    return arr


def main():
    print(check_board())


if __name__ == "__main__":
    main()
