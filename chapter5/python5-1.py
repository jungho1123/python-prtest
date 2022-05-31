#1~99까지 난수 10개로 리스트를 만들고 리스트, 정렬리스트, 내림차순 정렬 리스트를 출력하세요.
from random import *

lst=sample(range(1,100),10)
print('리스트 {}'.format(lst))
print('정렬 리스트 {}'.format(sorted(lst)))
print('역순 리스트 {}'.format(sorted(lst,reverse=True)))
