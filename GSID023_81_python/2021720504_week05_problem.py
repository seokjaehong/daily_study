from typing import List


def BubbleSort(arr: List[int]) -> List[int]:
    ### Edit Here ###

    # Bubble Sort

    #################
    for i in range(len(arr) - 1, 0, -1):
        is_change = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_change = True
        if not is_change:
            break
    return arr


def main():
    arr = list()

    ### Edit Here ###

    # read data from input.txt    
    # Sorting with BubbleSort method
    # save data to output.txt

    #################

    t = open("input.txt")
    arr = list(map(int, t.read().split('\n')[:-1]))
    output_arr = BubbleSort(arr)
    outfiles = [str(x) + '\n' for x in output_arr]
    with open('output.txt', 'w') as outfile:
        outfile.writelines(outfiles)


if __name__ == "__main__":
    main()
