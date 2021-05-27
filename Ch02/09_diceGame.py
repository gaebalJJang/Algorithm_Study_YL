"""
problem 9 : 주사위 게임
작성자 : 안예린 (girlwcode)
작성일 : 21-05-08
"""

import sys
sys.stdin = open ("input.txt", "rt")

n = int(input())
res = 0

for i in range(n) :
    tmp = input().split()
    tmp.sort()
    a, b, c =map(int, tmp)

    if a == b and b == c :
        money = 10000 + a*1000
    if a == b and a == c :
        money = 1000 + (a*100)
    if b == c :
        money = 1000 + b*100
    else:
        money = c * 100
    if money>res :
        res = money

print(res)