#!/usr/bin/python3
def uppercase(str):
    result = 0
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            result += ord(str[i]) - 32
            print(chr(result), end="")
        else:
            print(str[i])