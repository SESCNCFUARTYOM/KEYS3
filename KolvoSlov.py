# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
import math

if __name__ == "__main__":
    p = true
    n = int(input("n = "))
    i=2
    while i<math.sqrt(n):
        p = n%i
        if(t==0):
            p=false
    if p == true:
        print("1")
    else:
        print("0")

