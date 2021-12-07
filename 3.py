#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    n = 5
    s = n
    days = 2
    while days <= 10:
        n += 2
        s += n
        days += 1
    print(s)