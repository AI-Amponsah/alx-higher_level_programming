#!/usr/bin/python3
def print_sum(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
    else:
        i = 1
        add = 0
        while i <= n:
            add = add + int(argv[i])
            i = i + 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    print_sum(sys.argv)
