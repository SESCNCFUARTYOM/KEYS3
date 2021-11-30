# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    s=int(input("Введите сумму покупки:"))
    m1=0
    m2=0
    m5=0
    m10=0
    m100=0
    m500=0
    while s>0:
        if s>=500:
            s-=500
            m500+=1
        elif s>=100:
            s-=100
            m100+=1
        elif s>=10:
            s-=10
            m10+=1
        elif s>=5:
            s-=5
            m5+=1
        elif s>=2:
            s-=2
            m2+=1
        else:
            s-=1
            m1+=1
    print("500р - ", m500)
    print("100р - ", m100)
    print("10р - ", m10)
    print("5р - ", m5)
    print("2р - ", m2)
    print("1р - ", m1)