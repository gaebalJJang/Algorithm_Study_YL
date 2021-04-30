"""
학습 일자 : 21-04-30
ch0. 파이썬 기초 문법(선수지식)
"""
# sep 함수 : 각 값 구분자 함수
a,b,c = 1,2,3
print(a,b,c, sep=' ,')

# end 함수 : 각 변수의 끝 값에 출력 값 설정
print(a, end=' ,')
print(b, end=' ,')
print(c)

# 변수 입력과 연산자
a = input("숫자를 입력하세요 : ")
print(a)

# split() : 띄어쓰기로 입력 값 구분
a,b = input("숫자를 입력하세요 : ").split()
print(int(a)+int(b))

# map() : mapping 함수
a,b = map(int,input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 거듭 제곱

# type() : type 변환 함수
a = 4.3
b = 5
c = a+b
print(type(c)) # class 'float'

# 조건문 if (분기, 중첩)
x = 7
if x == 7 : # if x equals 7
    print("lucky")
elif x != 8 : # if x not equals 8 (다중 if 문)
    print("hi")
else :
    print("wow")

# 중첩 if 문
y = 15
if y >= 10:
    if y % 2 == 1:
        print("10이상의 홀수")

if x > 0 :
    if x < 10 :
        print("10보다 작은 양수") # equals to

if (x > 0 and x < 10) : # equals to 0<x<10 (python only)
    print("10보다 작은 양수")

if x > 0 :
    print("양수")
else : #분기문
    print("음수")


#반복문 (for, while)
a = range(10) # range() : 순차적 정수 배열 만드는 함수
print(list(a))

a = range(1,10)
print(list(a))

# for 문
for i in range(10) :
    print (i)

for i in range(10, 0, -1) : # 감소하는 for 문
    print (i)

# while 문
i = 1
while i <= 10 :
    print(i)
    i = i + 1 # i += 1

 무한 루프
while True :
    print(i)
    i += 1

# continue, break
for i in range(1,11) :
    if i % 2 == 0:
        continue # print(i) 무시하고 지나감
    print(i)
    if i == 5 :
        break # 강제 종료
else :
    print('d')

# ex1. 1부터 n 까지 홀수 출력하기
n = int(input())
for i in range (1,n+1) :
    if i % 2 == 1 :
        print(i)

# ex2. 1부터 n까지의 합 구하기
n = int(input())
for i in range (1,n+1) :
    sum = sum + i

print(sum)

# ex3. n의 약수 출력
n = int(input())
for i in range (1,n+1) :
    if n % i == 0:
        print(i , end =" ")

# 중첩 for 문
for i in range (5) :
    for j in range(5) :
        print("*", end = ' ')
    print()

for i in range(5) :
    for j in range(5-i) :
        print("*", end=' ')
    print()

# 문자열과 내장함수
msg = "It is Time"
print(msg.upper()) # upper() : 모든 문자 대문자로 변환
print(msg.lower()) # lower() : 모든 문자 소문자로 변환
print(msg) # 원 문자는 바뀌지 않음

print(msg.find('T')) # find() : T가 있는 인덱스 넘버를 리턴해줌
print(msg.count('T')) # count() : T의 갯수 리턴
print(msg[:2])  # It
print(msg[3:5]) # is

for i in range(len(msg)) :
    print(msg[i], end=' ')

for x in msg : #equals to
    print(x, end =' ')


for x in msg :
    if x.isupper(): # 대문자만 출력
        print(x, end =' ')

for x in msg :
    if x.isalpha(): # 알파벳만 출력 (공백 제거)
        print(x, end =' ')

tmp = 'AZ'
for x in tmp :
    print(ord(x)) # ASCII 넘버 출력
"""

"""
# 리스트와 내장함수 (1)
import random as r

b = list()  # equals to b = []
print(b)

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])  # 1

b = list(range(1, 11))
print(b)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = a + b
print(c)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.append(6)  # 6이라는 값 추가
a.insert(3, 7)  # 3번 자리에 7 추가
a.pop()  # 마지막 제거
print(a)
a.pop(3)  # 3번 자리 값 제거
print(a)

a.remove(4)  # 4 라는 값 제거
print(a.index(5))  # 5 값의 index num 출력

sum(a)
min(a)  # 리스트에서 최소 인자 값 출력
max(a)  # 리스트에서 최대 인자 값 출력

r.shuffle(a)  # a인자를 랜덤하게 셔플하기
print(a)

a.sort()  # 오름차순 sorting
a.sort(reverse=True)  # 내림차순 sorting

a.clear()  # 배열 초기화

# 리스트와 내장함수 (2)
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])

for i in range (len(a)) :
    print(a[i], end=' ')

for x in a : # equals to
    print(x, end=' ')


for x in a :
    if x % 2 == 1 :
        print(x, end=' ')

for x in enumerate(a): # enumerate() : 배열을 튜플값으로 변경
    print(x[0], x[1])

for index, value in enumerate(a): # equals to
    print(index, value)

if all(60 > x for x in a) : # all() : 모든 것이 참이면 참
    print("yes")
else:
    print("no")

if any(15>x for x in a) : # any() : 한개라도 참이면 참
    print("yes")
else:
    print("no")


# 2차원 리스트 생성과 접근
a = [0] * 10
print(a) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a = [[0]*3 for _ in range(3)] # 3*3 행렬 만들기
print(a)
a[0][1] = 1
print(a)
a[1][1] =2

for x in a : # x = 한 행
    print(x)

for x in a :
    for y in x :
        print(y, end=' ')
    print()



# 함수 만들기
def add(a, b):
    c = a+b
    print(c)

add(3, 2)

def add2(a,b) :
    c = a+b
    return c

x = add2(3,2)
print(x)

def add3(a,b) :
    c = a+b
    d = a-b
    return c, d # c++ 과 다르게, 여러 값을 튜플 형식으로 리턴

# ex4. 소수만 출력하는 함수 구현
def isPrime(x) :
    for i in range(2,x): # 2부터 자기 자신까지
        if x % i == 0: # 약수가 존재한다면
            return False
    return True # 약수가 존재하지 않으면, 소수

a = [12, 13, 7, 9, 19]

for y in a :
    if isPrime(y) :
        print(y, end=' ')

# 람다 함수 (익명의 함수)
def plus_one(x):
    return x+1

print(plus_one(1))

#plus_one()을 람다함수로 구현
plus_two = lambda  x : x +2
print(plus_two(1))

a = [1,2,3]
print(list(map(plus_one,a))) # map(함수, 인자)
print(list(map(lambda x : x+1, a))) # equals to


