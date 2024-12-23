#Variables and Some Arithmetic // idk why we are calculating the square of the hypotenuse instead of the hypotenuse itself.
import sys

def count_hypotenuse(in_file:str):
    with open(in_file, "r") as data:
        legs = (data.readlines()[0]).split()
        return (int(legs[0])**2 + int(legs[1])**2)

if __name__ == "__main__":
    print(count_hypotenuse(sys.argv[1]))
