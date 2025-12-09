

def validate1(datum):
    s = str(datum)
    len = len(s)

    if len%2 != 0:
        return True

    (a,b) = (s[0,len/2], s[(len/2+1):])
    
def part1(data):
    # print(data)
    invalid = []

    for d in data:
        (start, stop) = d.split("-")
        for s in range(int(start), int(stop)+1):
            if not validate1(s):
                invalid.append(s)

    print(invalid)


def read_data(file, delim="\n"):
    data = []
    with open(file) as f:
        data = f.read().split(delim)
    return data

def main():
    data_test = read_data("day02/example.txt", ",")
    # print(data_test)
    part1([data_test[0]])

if __name__ == "__main__":
    main()
