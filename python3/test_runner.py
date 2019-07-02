from time import time


def run(my_func, right_answer):
    start = time()
    answer = my_func()
    end = time()

    assert answer == right_answer

    print("Answer:", answer)
    print("Execution time:", end - start)


def my_func():
    print("Run my_func()")
    return "success"


def test():
    run(my_func, "success")


if __name__ == '__main__':
    test()
