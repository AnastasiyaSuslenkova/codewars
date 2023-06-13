#Given an integral number, determine if it's a square number

import math


def is_square(n):
    if n < 0:
        return False
    sq = math.sqrt(n)
    if sq == int(sq):
        return True
    return False


if __name__ == '__main__':
    print(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
    print(is_square(0), True, "0 is a square number (0 * 0)")
    print(is_square(3), False, "3 is not a square number")
    print(is_square(4), True, "4 is a square number (2 * 2)")
    print(is_square(25), True, "25 is a square number (5 * 5)")
    print(is_square(26), False, "26 is not a square number")
