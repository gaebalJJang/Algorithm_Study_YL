"""
problem 3 : K번째 큰 수
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""

import sys
sys.stdin = open("input.txt","rt")

n, k = map(int, input().split())
a = list(map(int,input().split()))

#set() :  중복을 제거하는 자료구조
res = set()

for i in range(n) :
    for j in range(i+1, n) :
        for x in range(j+1, n) :
           res.add(a[i]+a[j]+a[x]) # 모든 숫자의 합을 계산

res = list(res)
res.sort(reverse=True)

print(res[k-1])
