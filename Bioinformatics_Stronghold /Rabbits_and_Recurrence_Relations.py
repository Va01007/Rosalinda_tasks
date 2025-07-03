import sys


def Count_rabbits(in_file:str):
    with open(in_file, "r") as data:
        line = data.readlines()[0].split()
    bag = []
    res = {}
    k = int(line[0])
    n = int(line[1])
    Summ = 0
    s = 1 
    for d in range(k):
        bag.append(f"pair{d}")
    for fn, i in enumerate(range(k), start=2):
        if fn <= 3:
            #print(fn)
            res[bag[i]] = s
        elif fn == 4:
            res[bag[i]] = res[bag[i-2]]*n 
            res['pair0'] = 0
        else:
            res[bag[i]] = (sum(res.values()) - res[bag[i-1]])*n
    for ob in res:
        Summ += res[ob]
    return Summ


if __name__ == "__main__":
    print(Count_rabbits(sys.argv[1]))
