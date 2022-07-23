from random import *

C= list(sample(range(1,101),9))
F=list(map(lambda cels: cels*9/5+32,C))
print('섭씨 온도: {}'.format(C))
print('화씨 온도: {}'.format(list(map(lambda cels: cels*9/5+32,C))))
print()

for c,f in zip(C,F):
    print('섭씨 온도 {} => 화씨 {}'.format(c,f))
