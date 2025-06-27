import sys


def Calculate(in_file:str):
    with open(in_file, "r") as file:
        args = file.readlines()[0].split()
    calc_list = [2, 2, 2, 1.5, 1, 0]
    sum = 0
    for i, calc in zip(args, calc_list):
        sum +=  float(i) * calc
    return (sum)


if __name__ == "__main__":
    print(Calculate(sys.argv[1]))
