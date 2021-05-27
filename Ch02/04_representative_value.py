"""
problem 4 : 대표값
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
l = list(map(int,input().split()))

mean = round(sum(l) / n)
min = 100
num = 0

for i in range (n) :
    r = abs(mean - l[i]) # 편차 구하기
    if (r < min) : # 편차가 기준점보다 작다면
        num = i # 기준점 갱신
        min = r
    elif r == min : # 편차가 같다면
        if (l[num] < l[i]) : # 더 큰 수의 값으로 갱신
            num = i
            break

print(mean, r, l[i], num + 1)