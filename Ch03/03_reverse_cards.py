"""
problem 3 : 카드 역배치
작성자 : 안예린 (girlwcode)
작성일 : 21-05-18
"""

import sys
sys.stdin = open("input.txt", "r")
a = list(range(21))

for _ in range (10) :
    s, e = map(int, input().split())
    for i in range((e-s+1)//2) :
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop()
for x in a :
    print(x, end=' ')