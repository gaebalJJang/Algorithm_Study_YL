"""
problem 10 : 점수 계산
작성자 : 안예린 (girlwcode)
작성일 : 21-05-09
"""

import sys
sys.stdin = open ("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a :
    if x == 1 :
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)