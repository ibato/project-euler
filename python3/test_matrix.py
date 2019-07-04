from time import time


def get_empty_matrix(n):
    result = []
    for i in range(n):
        t = [0] * n
        result.append(t)
    return result


def test():
    assert len(get_empty_matrix(5)) == 5
    assert len(get_empty_matrix(5)[0]) == 5


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
