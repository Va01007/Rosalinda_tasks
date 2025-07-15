import sys
import random


def Order_String(in_file:str):
    res = []
    dict_for = {}
    dict_rev = {}
    with open(in_file, "r") as file:
        lines = file.readlines()
        symbols = lines[0].split()
        pos = int(lines[1])
        for num, bukva in enumerate(symbols):
            dict_for[bukva] = num
            dict_rev[num] = bukva
        symbols_code = [dict_for[k] for k in symbols]
    for k in range(1, pos+1):
        temp_res = []
        while len(temp_res) != (len(symbols_code) ** k):
            sam = random.sample((symbols_code * k), k)
            if sam not in temp_res:
                temp_res.append(sam)
        res = res + temp_res
    for i in sorted(res):
        temp_line = ""
        for S in i:
            temp_line += dict_rev[S]
        print(temp_line)


if __name__ == "__main__":
    Order_String(sys.argv[1])

#Ordering Strings of Varying Length Lexicographically
