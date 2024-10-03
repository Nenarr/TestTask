import sys


def Solution(*args):
    lst = []
    i = 1
    while True:
        lst.append(i)
        i = 1 + (i + b - 2) % a
        if i == 1:
            return lst


if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(''.join(map(str, Solution(a, b))))
