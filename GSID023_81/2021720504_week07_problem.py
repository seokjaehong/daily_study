class Student:
    def __init__(self):
        ### Edit Here ###

        # get name, major, and id_num

        #################
        self.name = input("이름을 입력하세요:")
        self.major = input("전공을 입력하세요:")
        self.id_num = input("학번을 입력하세요:")

    def display(self):
        ### Edit Here ###

        # print information

        #################
        print(f'{self.name}의 전공은 {self.major}이며, 학번은 {self.id_num}입니다.')


class Undergraduate(Student):
    def __init__(self):
        ### Edit Here ###

        # get name, major, id_num, and submajor

        #################
        super().__init__()
        self.submajor = input("부전공을 입력하세요:")

    def display(self):
        ### Edit Here ###

        # print information

        #################

        super().display()
        print(f'{self.name}의 부전공은 {self.submajor}입니다.')


class Graduate(Student):
    def __init__(self):
        ### Edit Here ###

        # get name, major, id_num, and coursetype

        #################
        super().__init__()
        self.coursetype = input("소속과정을 입력하세요:")

    def display(self):
        ### Edit Here ###

        # print information

        #################
        super().display()
        print(f'{self.name}의 부전공은 {self.coursetype}입니다.')


def Choose_type() -> int:
    ### Edit Here ###

    # choose type of student

    #################
    type = int(input('입력할 학생의 종류를 선택하세요 (1: 일반, 2: 학사과정, 3: 대학원과정, -1: 종료)'))
    return type


def main():
    while True:
        type = Choose_type()

        if type == 1:
            student = Student()
        elif type == 2:
            student = Undergraduate()
        elif type == 3:
            student = Graduate()
        elif type == -1:
            break

        student.display()


if __name__ == "__main__":
    main()
