#float.fromhex(str)을 이해하고 두 16진수 실수를 입력받아 사칙연산을 수행하는 프로그램 작성
#float.fromhex(str)은 16진수 형태의 문자열 str을 실수로 변환

n1 = input('첫 번째 16진수 실수 입력 >> ')
n2 = input('두 번째 16진수 실수 입력 >> ')

N1 = float.fromhex(n1)
N2 = float.fromhex(n2)

print('실수1: {} 실수2: {}'.format(N1,N2))
print('합: {}'.format(N1+N2))
print('차: {}'.format(N1-N2))
print('곱하기: {}'.format(N1*N2))
print('나누기: {}'.format(N1/N2))
