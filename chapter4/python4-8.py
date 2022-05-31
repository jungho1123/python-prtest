#난수로 발생시킨 1~100까지의 첫 번째 피연산자와 사용자가 표준입력한 연산자, 두 번째 표준입력한 피연산자를 계산해 출력하시오
#연산자가 +-*/%가 아니라면 종료
import random

num1=random.randint(1,101)
print('첫 값은 {}이다.'.format(num1))

while True:
    a=input('산술 연산의 종류를 입력하세요. >> ')
    if a!='+' and a!='-' and a!='*' and a!='/' and a!='%':
        break
    num2=int(input('두 번째 피연산자를 입력하세요. >> '))

    if a=='+':
         print('{} + {} = {}'.format(num1,num2,num1+num2))
    elif a=='-':
         print('{} - {} = {}'.format(num1,num2,num1-num2))
    elif a=='*':
         print('{} * {} = {}'.format(num1,num2,num1*num2))
    elif a=='/':
         print('{} / {} = {:.1f}'.format(num1,num2,num1/num2))
    elif a=='%':
         print('{} % {} = {:.1f}'.format(num1,num2,num1%num2))
    else:
        break

print('종료'.center(30,'*'))
