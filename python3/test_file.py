from time import time
import os


def open_file(rel_path):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, "r")
    return f


def test():
    open_file("./test_042_words.txt")


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
