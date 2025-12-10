import math
from operator import itemgetter, attrgetter

def read_data(file, delim="\n"):
    data = []
    with open(file) as f:
        data = f.read().split(delim)
    return data

def per_element_process(a, b):
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)

def create_all_pairs(data):    
    pairs = []
    for start_ix in range(0, len(data)):
        for i in range(start_ix+1, len(data)):
            pairs.append((per_element_process(data[start_ix], data[i]), (start_ix, i)))

    sorted_pairs = sorted(pairs, key=itemgetter(0), reverse=True)
    return sorted_pairs

def process1(data):
    dd = []
    for d in data:
        ss = (d.split(","))
        ii = [int(s) for s in ss]
        dd.append((ii[0], ii[1]))
    return dd

def part1(data):
    sorted_data = create_all_pairs(data)

    for i in sorted_data:
        print(i)

    print("largest area ", sorted_data[0])

def main():
    # data_test = read_data("day09/example.txt")
    # data_test = process1(data_test)

    # # for i, d in enumerate(data_test):
    # #     print("{index}: {coord}".format(index=i, coord=d))

    # part1(data_test)

    # data_test = read_data("day09/full.txt")
    # data_test = process1(data_test)
    # part1(data_test)

    data_test = read_data("day09/example.txt")
    data_test = process1(data_test)

    # for i, d in enumerate(data_test):
    #     print("{index}: {coord}".format(index=i, coord=d))

    part1(data_test)

if __name__ == "__main__":
    main()
