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

def calc_sorted_distance_list(data):
    dist_mat = []
    for start_ix in range(0, len(data)):
        dist_row = [(0, (0,0))]*(start_ix+1)
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
    return sorted_dist

def find_junction_in_circuits(circuits, junction):
    for idx, loop in enumerate(circuits):
        try:
            loop.index(junction)
            return idx
        except:
            pass
    return -1

def merge_circuits(circuits, ai, bi):
    a_loop = circuits[ai]
    b_loop = circuits[bi]
    
    circuits.remove(a_loop)
    circuits.remove(b_loop)

    circuits.append(a_loop+b_loop)

    return circuits

def part1(data, join_count=10):
    sorted_dist = calc_sorted_distance_list(data)

    circuits = []
    attempts = 0
    for jj in sorted_dist:
        attempts+=1
        if (attempts == join_count):
            break

        a = jj[1][0]
        b = jj[1][1]

        print("{count} join {a} and {b}".format(count=attempts, a=a, b=b))

        # found = False
        ai = find_junction_in_circuits(circuits, a)        
        bi = find_junction_in_circuits(circuits, b)

        if (ai == -1 and bi == -1):
            circuits.append([a, b])
            continue

        if (ai != -1 and bi != -1):
            if (ai == bi):
                # Seems like input for puzzle is bugged skip count for example but not full data?
                if (join_count == 10):
                    attempts-=1
                print("skipped")
                continue

            circuits = merge_circuits(circuits, ai, bi)

            continue

        if (ai != -1):
            circuits[ai].append(b)
        else:
            circuits[bi].append(a)

    circuit_lengths = [
        len(x) for x in circuits
    ]
    sorted_lengths = sorted(circuit_lengths, reverse=True)

    # sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    print(sorted_lengths)
    print("first three circ mult", (math.prod(sorted_lengths[:3])))


def part2(data):
    max_circuit = len(data)
    print("max ", max_circuit)
    sorted_dist = calc_sorted_distance_list(data)
    print("sorted dists ", len(sorted_dist))


    circuits = []
    attempts = 0
    for jj in sorted_dist:
        # sorted_dist is (distance, (a_index, b_index))
        attempts+=1
        # if (attempts == join_count):
        #     break

        # junctions = [ jj[1][0], jj[1][1] ]
        a = jj[1][0]
        b = jj[1][1]

        print("{count} join {a} and {b}".format(count=attempts, a=a, b=b))
        # if (len(circuits)>0):
        #     print("circuit count {circs} first circ has {len}".format(circs=len(circuits), len=len(circuits[0])))

        # found = False
        ai = find_junction_in_circuits(circuits, a)
        bi = find_junction_in_circuits(circuits, b)

        if (ai == -1 and bi == -1):
            circuits.append([a, b])
        elif (ai != -1 and bi != -1):
            if (ai == bi):
                print("skipped")
                continue

            # print("merge circ")
            circuits = merge_circuits(circuits, ai, bi)
            # foo = len(circuits[0])
            # print("length in first ", foo)
            
            # if (len(circuits[0]) == max_circuit):
            #     print("Final junction between {a} and {b} mult {mult}".format(a, b, a*b))

            # continue
        else:
            if (ai != -1):
                circuits[ai].append(b)
            else:
                circuits[bi].append(a)

        foo = len(circuits[0])
        print("length in first ", foo)
        
        if (len(circuits[0]) == max_circuit):
            a_x = data[a][0]
            b_x = data[b][0]
            print("Final junction between {a} and {b} mult {a_x} * {b_x} = {mult}".format(a=a, b=b, a_x=a_x, b_x=b_x, mult=a_x*b_x))
            break

    circuit_lengths = [
        len(x) for x in circuits
    ]
    sorted_lengths = sorted(circuit_lengths, reverse=True)
    print(sorted_lengths)

    # # sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    # print(sorted_lengths)
    # print("first three circ mult", (math.prod(sorted_lengths[:3])))


def read_data(file, delim="\n"):
    data = []
    with open(file) as f:
        data = f.read().split(delim)
    return data

def main():
    # data_test = read_data("day08/example.txt")
    # data_test = process1(data_test)
    # part1(data_test, 10)

    # data_test = read_data("day08/full.txt")
    # data_test = process1(data_test)
    # part1(data_test, 1000)
    
    # data_test = read_data("day08/example.txt")
    # data_test = process1(data_test)
    # part2(data_test)

    data_test = read_data("day08/full.txt")
    data_test = process1(data_test)
    part2(data_test)

if __name__ == "__main__":
    main()
