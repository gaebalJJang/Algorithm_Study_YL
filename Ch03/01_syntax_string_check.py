"""
problem 1 : 회문 문자열 검사
작성자 : 안예린 (girlwcode)
작성일 : 21-05-15
"""

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))