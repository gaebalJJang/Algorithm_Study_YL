"""
problem 2 : K번째 수
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""
import sys
sys.stdin = open("input.txt","rt")

T = int(input())

for t in range (T) :
    N, s, e ,k = map(int, input().split())
    l = []
    l[0:N] = map(int, input().split())
    # cf. l = list(map(int, input().split())) 가 더 좋은 표현

    f = l[s-1:e]
    f.sort()
    print('#',t+1 ,f[k-1]) # print('#%d %d' %(t+1, l[k-1]))
