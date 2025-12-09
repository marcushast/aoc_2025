import math

raw_test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


# This is horrible. It would be nice to rewrite it as
#   1 - with list comprehensions
#   2 - as branchless code

def convert(s):
    s = s.replace("L", "-")
    s = s.replace("R", "")
    i = int(s)
    return i

def prep_data(data):
    int_list = []
    for s in data:
        # s = s.replace("L", "-")
        # s = s.replace("R", "")
        # i = int(s)
        int_list.append(convert(s))
    return int_list

def part1(dial, data):
    current = dial
    count_zero = 0
    for s in data:
        current = (current + s) % 100
        if current == 0:
            count_zero += 1

    print("count_zero ", count_zero)

def part2(dial, data):
    current = dial
    point_zero = 0

    for s in data:
        i = convert(s)
        print("Current {current} apply {rot}".format(current=current, rot=s))

        new_pos = (current + i) % 100
        hundreds = abs(i) // 100
        #rem = math.trunc(math.remainder(-123, 100))

        if current != 0:
            if i < 0:
                if new_pos > current:
                    point_zero+=1
                elif new_pos == 0:
                    point_zero+=1
            elif i > 0:
                if new_pos < current:
                    point_zero+=1

        point_zero+=hundreds
        current = new_pos

        print("New pos {current} point zero {zero}".format(current=current, zero=point_zero))


    print("point zero ", point_zero)

def main():
    data_test = raw_test.splitlines()
    # data_test = prep_data(data_test)

    fileopen = open("day01/data01_1.txt")
    data_full = fileopen.read().splitlines()
    # data_full = prep_data(data_full)

    # print("data ", data[:10])

    # part1(50, data)
    part2(50, data_full)
        
if __name__ == "__main__":
    main()