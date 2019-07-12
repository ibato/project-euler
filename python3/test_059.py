from time import time
from itertools import product
import test_file as file
import test_runner as runner


def solve():
    answer = 0
    c = [chr(x) for x in range(97, 123)]
    f = file.open_file("test_059_cipher.txt")
    encrypted = f.readline().strip().split(",")
    for each in product(c, repeat=3):
        decrypted = ""
        for i in range(len(encrypted)):
            d = int(encrypted[i]) ^ ord(each[i % 3])
            decrypted = decrypted + chr(d)
        if not decrypted.find('the') == -1 and decrypted.find(' ') != -1 and decrypted.find(' a ') != -1 and decrypted.find('.') != -1:
            answer = sum([ord(decrypted[i]) for i in range(len(decrypted))])
            break
    f.close()
    return answer


def test():
    right_answer = 129448
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
