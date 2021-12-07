#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    S = int(input())
    n500 = 0
    n100 = 0
    n10 = 0
    n5 = 0
    n2 = 0
    n1 = 0
    while S > 0:
        if S >= 500:
            n500 += 1
            S -= 500
        elif S >= 100:
            n100 += 1
            S -= 100
        elif S >= 10:
            n10 += 1
            S -= 10
        elif S >= 5:
            n5 += 1
            S -= 5
        elif S >= 2:
            n2 += 1
            S -= 2
        elif S >= 1:
            n1 += 1
            S -= 1

    print("500 -", n500)
    print("100 -", n100)
    print("10 -", n10)
    print("5 -", n5)
    print("2 -", n2)
    print("1 -", n1)
