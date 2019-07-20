from time import time
from time import sleep
from datetime import timedelta
import threading


def run(my_func, right_answer):
    start = time()
    timer = threading.Timer(10.0, log, args=(start,))
    timer.start()
    answer = my_func()
    end = time()
    timer.cancel()

    assert answer == right_answer

    print("Answer:", answer)
    print("Execution time:", end - start)


def my_func():
    print("Run my_func()")
    return "success"

def log(start):
    print("Info: %s" % (timedelta(seconds=time() - start)))

def test():
    run(my_func, "success")


if __name__ == '__main__':
    test()
