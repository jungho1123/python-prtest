from random import *

dcs={'가위':'보오','바위':'가위','보오':'바위'}
tit=['철수','영희','승자','비김']
rsp=('가위','바위','보오')

b=0  #비김
c=0  #철수 이김
d=0  #영희 이김

print('*'*24)
print('{:5} {:5} {:5}'.format(tit[0],tit[1],tit[2]))
print('*'*24)

for i in range(20):
    cs=choice(rsp)
    yh=choice(rsp)
    if cs==yh: #비김
        a=3
        b+=1
        print('{:5} {:5} {:5} {:2}'.format(cs,yh,tit[a],b))

    elif dcs[cs]==yh: #철수 이김
        a=0
        c+=1
        print('{:5} {:5} {:5} {:2}'.format(cs,yh,tit[a],c))

    else:     #영희 이김
        a=1
        d+=1
        print('{:5} {:5} {:5} {:2}'.format(cs, yh, tit[a], d))

print()
print('총 게임 회수: {} 비긴 회수: {}'.format(20,b))
print('철수 승률: {}'.format(c/20))
print('영희 승률: {}'.format(d/20))
