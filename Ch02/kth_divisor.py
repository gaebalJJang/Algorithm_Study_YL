"""
problem 1 : K번째 약수
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""
N,K = map(int,input().split())

if N >=1 and N <= 10000 :
    if K >= 1 and K <= 10000 :
        l = []
        for i in range (1,N) :
            if N % i == 0 :
                l.append(i)
        print(l[K-1])
    else :
        K = input("K를 다시 입력하세요 :")
else: N = input("N를 다시 입력하세요 :")

