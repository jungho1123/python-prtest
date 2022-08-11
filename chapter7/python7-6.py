from random import *

def three(n):
    if n%3==0:
        return True
    else:
        return False

lst=list(sorted(sample(range(1,31),6))) #1부터 30까지 정수 중 랜덤으로 6개 출력
print('원 리스트: {}'.format(lst))
lst2=list(filter(three,lst))
print('필터 리스트: {}'.format(lst2))
