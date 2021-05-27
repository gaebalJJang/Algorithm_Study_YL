"""
problem 6 : 자리수의 합
작성자 : 안예린 (girlwcode)
작성일 : 21-05-06
"""
import sys
sys.stdin=open("input.txt","rt")
a = int(input())

"""
# python 내장 함수를 사용하지 않았을 때,
def digit_sum(x) :
    sum = 0
    while x > 0 :
        sum += x % 10 # 10으로 나눈 목
        x=x//10 # 10으로 나눈 나머지

"""

# python 내장 함수 사용시,
def digit_sum(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum

max = -2147000000

for x in a :
    tot = digit_sum(x)
    if tot>max :
        max = tot
        res = x

print(res)


