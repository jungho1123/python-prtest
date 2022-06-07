#함수 factorial(n)을 정의해 다음과 같이 출력하는 프로그램을 작성하시오.

def factorial(n):
    for i in range(1,n):
        n*=i
    return n

print('5! = {}'.format(factorial(5)))
print('10! = {}'.format(factorial(10)))
print('20! = {}'.format(factorial(20)))
