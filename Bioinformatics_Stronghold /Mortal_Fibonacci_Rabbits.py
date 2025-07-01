import sys


def Count_rabbits(in_file:str):
    with open(in_file, "r") as file:
        line = file.readline()
        n = int(line.split()[0])
        m = int(line.split()[1])
        start_point = 1
        res = {loop:0 for loop in range(n)}
        for iter in res.keys():
            if iter <= 1:
                res[iter] = 1
            else:
                res[iter] = res[iter - 1] + res[iter - 2]
            if (iter - m) in res:
                del_val = res[iter - m]
                for pair in res.keys():
                    if res[pair] == 0:
                        continue
                    res[pair] -= del_val
        return res[list(res.keys())[-1]]


if __name__ == "__main__":
    print(Count_rabbits(sys.argv[1]))
