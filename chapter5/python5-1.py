from random import *

lst=sample(range(1,100),10)
print('리스트 {}'.format(lst))
print('정렬 리스트 {}'.format(sorted(lst)))
print('역순 리스트 {}'.format(sorted(lst,reverse=True)))
