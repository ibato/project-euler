from time import time
import test_combinatorics as cb
import test_file as file
import test_runner as runner


def royal_flush(rank, card):
    s = score(rank, straight_flush(0, card))
    if s % 100 == CARD["A"]:
        return s
    return 0


def straight_flush(rank, card):
    if not straight(0, card) == 0 and not flush(0, card) == 0:
        return score(rank, card[0][0])
    return 0


def four_of_a_kind(rank, card):
    return pair(rank, card, 1, 4)


def full_house(rank, card):
    t = three_of_a_kind(0, card)
    p = one_pair(0, card)
    if not t == 0 and not p == 0:
        return score(rank, t)
    return 0


def flush(rank, card):
    if len([1 for i in range(1, len(card)) if not card[i][1] == card[i - 1][1]]) == 0:
        return score(rank, card[0][0])
    return 0


def straight(rank, card):
    if len([1 for i in range(1, len(card)) if card[i][0] - card[i - 1][0] == -1]) == 4:
        return score(rank, card[0][0])
    return 0


def three_of_a_kind(rank, card):
    return pair(rank, card, 1, 3)


def two_pair(rank, card):
    return pair(rank, card, 2, 2)


def one_pair(rank, card):
    return pair(rank, card, 1, 2)


def pair(rank, card, kind, same):
    highest = []
    for i in CARD.values():
        p = list(filter(lambda x: i == x[0], card))
        if len(p) == same:
            highest.append(p[0][0])
    if len(highest) == kind:
        return score(rank, max(highest))
    return 0


def score(rank, highest):
    return rank * 100 + highest


def rank(card):
    for i in range(len(FUNC)):
        r = FUNC[i](i + 1, card)
        if not r == 0:
            return r
    return 0


def highest(cards):
    return [cards[0][i][0] - cards[1][i][0] for i in range(len(cards[0])) if not cards[0][i][0] == cards[1][i][0]][0]


def convert(line):
    return (sorted(map(lambda x: (CARD[x[0]], x[1]), line[:5]), reverse=True),
            sorted(map(lambda x: (CARD[x[0]], x[1]), line[5:]), reverse=True))


def is_player1_winner(cards):
    r = (rank(cards[0]), rank(cards[1]))
    # 1. compare rank and the number made up of that
    if r[0] > r[1]:
        return True
    # 2. if they have the same rank, compare numbers
    if r[0] == r[1] and highest(cards) > 0:
        return True
    return False


CARD = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
FUNC = [one_pair, two_pair, three_of_a_kind, straight, flush, full_house,
        four_of_a_kind, straight_flush, royal_flush]


def solve():
    with file.open_file('./test_054_poker.txt') as f:
        answer = sum(
            map(is_player1_winner, [convert(line.rstrip().split()) for line in f]))
    return answer


def test():
    right_answer = 376
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
