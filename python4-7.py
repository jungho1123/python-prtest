#정수 1개를 표준 입력으로 받아 소수인지를 판별하시오.
num=int(input('소수인지를 판별할 2 이상의 정수 입력>> '))

for i in range(2,num-1):
    if num%i==0:
        a=1
    else:
        a=2

if a==1:
    print()
else:
    print('정수 {}은 소수이다.'.format(num))