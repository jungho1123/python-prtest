#1~99까지 정수인 난수 2개를 생성하고 곱하기의 결과를 출력하는 프로그램을 작성하시오.
import random

num1=random.randint(1,100)
num2=random.randint(1,100)
print('{} * {} = {}'.format(num1, num2, num1*num2))

while True:
    a=input('계속 y/n ?')
    if a=='y':
        print('{} * {} = {}'.format(num1, num2, num1 * num2))
    else:
        break





