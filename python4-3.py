#1부터 99까지 임의의 난수를 3개 지정하고 가장 큰 정수를 출력하세요
import random
from random import randint

for i in range(3):
    num=random.randint(1,100)
    print('{}'.format(num),end=' ')

print('중에서 최대: {}'.format(num))
