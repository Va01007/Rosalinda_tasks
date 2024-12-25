import sys


def count_words(in_file:str):
    words_dict = {}
    with open(in_file, "r") as data:
        for word in (data.readlines()[0]).split():
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    for item in words_dict:
        print(f"{item} {words_dict[item]}")


if __name__ == "__main__":
    count_words(sys.argv[1])
