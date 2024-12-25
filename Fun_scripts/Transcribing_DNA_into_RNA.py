import sys


def to_rna(in_file:str):
    data =  open(in_file, mode="r")
    line = data.readlines()[0]
    a = ""
    for symbol in line:
        if symbol == "T":
            symbol = "U"
            a = symbol + a
        else:
            a = symbol + a
    data.close()
    return a[::-1]



if __name__ == "__main__":
    print(to_rna(sys.argv[1]))



#Why I think it's funny?
#I caught myself doing this just for one function. But I enjoy this strange decision a little bit.