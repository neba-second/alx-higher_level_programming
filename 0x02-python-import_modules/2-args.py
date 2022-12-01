#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{:d} argument:".format(count - 1))
        print("{:d}: {}".format(count - 1, sys.argv[1]))
    elif count > 2:
        print("{:d} arguments:".format(count - 1))
        for i in range(1, count):
            print("{:d}: {}".format(i, sys.argv[i]))
