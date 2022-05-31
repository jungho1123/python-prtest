#정수 하나와 2의 지수승으로 사용할 정수를 입력받아 연산자 <<와 **을 사용해 각각 계산한 결과가 같음을 보이는 프로그램을 작성하세요.
num=int(input('정수 입력 >> '))
a=int(input('2의 지수승 입력 >> '))
print()
print('정수 {} << {}, 결과: {}'.format(num, a, num << a))
print('정수 {} * {}**{}, 결과: {}'.format(num, 2, a, num*2**a))
print('2진수(32비트): {:32b} 정수: {}'.format(num, num))
print('2진수(32비트): {:32b} 정수: {} << {}'.format(num << a, num, a))
print('2진수(32비트): {:32b} 정수: {} * {}**{}'.format(num*2**a, num, 2, a))
