num=int(input('네 자리 정수 입력: '))
a=int(num/1000)
b=int((num-1000*a)/100)
c=int((num-1000*a-100*b)/10)
d=num-1000*a-100*b-10*c

print('{}{}{}{}'.format(d,c,b,a))