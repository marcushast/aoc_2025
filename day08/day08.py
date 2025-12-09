import math
from operator import itemgetter, attrgetter

def euclid_dist(p1, p2):
    return math.sqrt(
        math.pow(p1[0]-p2[0], 2) # use a**2 instead
        + math.pow(p1[1]-p2[1], 2)
        + math.pow(p1[2]-p2[2], 2)
    )


def process1(data):
    dd = []
    for d in data:
        ss = (d.split(","))
        ii = [int(s) for s in ss]
        dd.append(ii)
    return dd

def part1(data):
    # print(data)
    dist_mat = []
    for start_ix in range(0, len(data)):
        # start_ix = 0
        dist_row = [(0, (0,0))]*(start_ix+1)
        # print(dist_row)
        for i in range(start_ix+1, len(data)):
            dist_row.append((euclid_dist(data[start_ix], data[i]), (start_ix, i)))
        dist_mat.append(dist_row)
    
    all_dists = [
        x
        for xs in dist_mat
        for x in xs
    ]
    
    all_dists = [ 
        x for x in all_dists if (x != (0, (0,0)))
    ]
    sorted_dist = sorted(all_dists, key=itemgetter(0))

    for x in sorted_dist[:10]:
        print(x)

    circuits = []
    attempts = 0
    for jj in sorted_dist:
        attempts+=1
        junctions = [ jj[1][0], jj[1][1] ]

        found = False
        for i in range(0, len(circuits)):
            if (circuits[i].find(junctions[0]) or circuits[i].find(junctions[1])):
                circuits[i].append(junctions)
                found = True

        if not found:
            circuits.append(junctions)
            
        if (attempts == 10):
            break
    
    print(circuits)

def read_data(file, delim="\n"):
    data = []
    with open(file) as f:
        data = f.read().split(delim)
    return data

def main():
    data_test = read_data("day08/example.txt")
    data_test = process1(data_test)
    part1(data_test)

if __name__ == "__main__":
    main()
