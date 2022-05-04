def isdigit_temp(temp):
    return temp.isdigit() or \
           (temp[0] == "+" and temp[1:].isdigit()) or \
           (temp[0] == '-' and temp[1:].isdigit())


def C2F():
    temp_c = input("섭씨 온도(C)를 입력하세요:")
    while not isdigit_temp(temp_c):
        temp_c = input("섭씨 온도(C)를 입력하세요:")
    temp_f = round((9.0 / 5.0) * float(temp_c) + 32, 1)
    print(f"섭씨 온도(C) {temp_c}도는 화씨 온도(F) {round(temp_f, 1)}도 입니다.")


### Edit Here ###
# get Celsius
# change scale to Fahrenheit
# print result
#################


def F2C():
    temp_f = input("화씨 온도(f)를 입력하세요:")
    while not isdigit_temp(temp_f):
        temp_f = input("화씨 온도(f)를 입력하세요:")
    temp_c = round(((5 * float(temp_f)) - 160) / 9.0, 1)
    print(f"화씨 온도(F) {temp_f}도는 섭씨 온도(C) {temp_c}도 입니다.")


def Choose_mode() -> int:
    ### Edit Here ###
    # choose scale change mode
    #################
    print("섭씨 온도(C)에서 화씨 온도(F)로 변환 = 1")
    print("화씨 온도(F)에서 섭씨 온도(C)로 변환 = 2")
    choice = input("선택하세요: ")
    while not (choice == "1" or choice == '2'):
        choice = input("선택하세요: ")
    return int(choice)


def Continue() -> bool:
    ### Edit Here ###
    # ask to continue
    #################
    cont = input("계속 하시겠습니까? (y/n):")
    while not (cont == 'y' or cont == 'n'):
        cont = input("계속 하시겠습니까? (y/n):")
    return cont == 'y'


def main():
    while True:
        print("단위환산")
        choice = Choose_mode()
        if choice == 1:
            C2F()
        elif choice == 2:
            F2C()
        if not Continue():
            break


if __name__ == "__main__":
    main()
