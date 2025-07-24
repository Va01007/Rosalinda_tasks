import sys
import math


def Random_string(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()
        DNA = lines[0][:-1]
        numbers = list(map(float, lines[1].split()))
        result = []
        for i in numbers:
            temp_value = 0
            for nucl in DNA:
                if nucl == "A" or nucl == "T":
                    temp_value += math.log10((1-i)/ 2)
                else:
                    temp_value += math.log10(i/2)
            result.append(round(temp_value, 3))
    return " ".join(map(str, result))


if __name__ == "__main__":
    print(Random_string(sys.argv[1]))
