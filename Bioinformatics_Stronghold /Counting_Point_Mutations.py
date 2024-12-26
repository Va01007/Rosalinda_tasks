import sys


def count_point_mutations(in_file:str):
    with open(in_file, "r") as data:
        lines = data.readlines()
        line1 = lines[0]
        line2 = lines[1]
        miss_matches = 0
        for nucl1, nucl2 in zip(line1, line2):
            if nucl1 != nucl2:
                miss_matches += 1
    return miss_matches


if __name__ == "__main__":
    print(count_point_mutations(sys.argv[1]))
