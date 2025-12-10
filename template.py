import math
from operator import itemgetter, attrgetter

def read_data(file, delim="\n"):
    data = []
    with open(file) as f:
        data = f.read().split(delim)
    return data

def process1(data):
    dd = []
    for d in data:
        ss = (d.split(","))
        ii = [int(s) for s in ss]
        dd.append(ii)
    return dd

def part1(data):
    pass

def main():
    data_test = read_data("dayNN/full.txt")
    data_test = process1(data_test)
    part1(data_test)

if __name__ == "__main__":
    main()
