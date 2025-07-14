import math
import random
import sys


def Enumerate_gene_orders(in_file:str):
    res = []
    with open(in_file, "r") as file:
        x = int(file.readline())
    list_val = [[i, -i] for i in range(1, x+1)]
    all_lists = []
    while len(all_lists) != math.factorial(x):
        shuf = random.sample(list_val, len(list_val))
        if shuf not in all_lists:
            all_lists.append(shuf)
    counter = 0
    for shu in all_lists:
        while counter <= 1000:
            string_val = ""
            for item in shu:
                string_val += f"{random.choice(item)}\t"
            if string_val not in res:
                res.append(string_val)
                counter = 0
            else:
                counter += 1
        counter = 0
    print(len(res))
    [print(k) for k in res]


if __name__ == "__main__":
    Enumerate_gene_orders(sys.argv[1])

#its stupid solution and uneffective but it works
