"""
problem 7 : 소수 (에라토스테네스 체)
작성자 : 안예린 (girlwcode)
작성일 : 21-05-08
"""
import sys
sys.stdin=open("input.txt","rt")
num = int(input())

cnt = 0

for i in range (2, num+1) :
    c = 0
    for j in range (1, i+1) :
        if(i % j == 0) :
            c += 1

        if (c >= 3) :
            break

    if (c == 2) :
        cnt += 1

print(cnt)