"""
problem 5 : 정다면체
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""
import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
a = [0] * (m+n)
b = list()
max = 0

for i in range (1, n+1) :
    for j in range(1, m+1) :
        sum = i + j
        a[sum-1] += 1

for k in range(len(a)) :
    if a[k] > max :
        max = a[k]

for t in range(len(a)) :
    if a[t] == max :
        print(t+1,end=" ")


