# 1리터는 0.264갤론, 1갤론은 3.785리터

def toliter():
    gallon=int(input('변환할 갤론은? '))
    liter=gallon*3.785
    print('{:.2f} 갤론 == {:.2f} 리터'.format(gallon,liter))

def togallon():
    liter=int(input('변환할 리터는? '))
    gallon=liter*0.264
    print('{:.2f} 리터 == {:.2f} 갤론'.format(liter,gallon))

num=int(input('번호 선택 1. 갤론 => 리터 2. 리터 => 갤론 '))

if num==1:
    toliter()

if num==2:
    togallon()
