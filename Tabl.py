# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    n=10
    a=1
    b=1
    for a in range(n):
        for b in range(n):
            c=a*b
            print(a, "*",b, "=", c)