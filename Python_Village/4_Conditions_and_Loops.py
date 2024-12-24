import sys

def sum_odd(in_file:str):
    s_odds = 0
    with open(in_file, "r") as data:
        breaks = list(map(int, data.readlines()[0].split()))
        for number in range(breaks[0], breaks[1] + 1):
            if number % 2 == 1:
                s_odds += number
    return s_odds
if __name__ == "__main__":
    print(sum_odd(sys.argv[1]))
