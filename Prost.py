# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
import math

if __name__ == "__main__":
    n = int(input("n = "))
    if n == 1:
        print(0)
    else:
        count = 0
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                count = count + 1
        if count == 0:
            print(1)
        else:
            print(0)
