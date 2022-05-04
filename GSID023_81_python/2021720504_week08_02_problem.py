import numpy as np
from typing import List


def moving_average(arr, window_size=3) -> List[int]:
    ### edit here

    #################
    ret = np.cumsum(arr, dtype=float)
    ret[window_size:] = ret[window_size:] - ret[:-window_size]
    return ret[window_size - 1:] / window_size


def main():
    print(np.arange(20))
    print(moving_average(np.arange(20), window_size=8))
    print([1, 2, 3, 7, 9])
    print(moving_average([1, 2, 3, 7, 9], window_size=3))


if __name__ == "__main__":
    main()
