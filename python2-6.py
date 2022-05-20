#두 정수를 입력받아 산술연산 /, %, //, ** 4개를 수행해 결과를 출력하는 프로그램을 작성하시오

n1=int(input('enter first number : '))
n2=int(input('enter second number : '))
print('{} / {} ==> {}'.format(n1,n2,n1/n2))
print('{} % {} ==> {}'.format(n1,n2,n1%n2))
print('{} // {} ==> {}'.format(n1,n2,n1//n2))
print('{} ** {} ==> {}'.format(n1,n2,n1**n2))
