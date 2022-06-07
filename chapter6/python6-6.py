#1~20까지의 난수 5개를 두 번 얻어 변수 A,B에 저장한다. A,B의 합집합, 교집합, 차집합, 여집합을 구해 출력하시오.

from random import *

A=set(sample(list(range(1,21)),5))
B=set(sample(list(range(1,21)),5))

print('A = {}'.format(A))
print('B = {}'.format(B))
print()
print('A | B = {}'.format(A|B))
print('A & B = {}'.format(A&B))
print('A - B = {}'.format(A-B))
print('A ^ B = {}'.format(A^B))
