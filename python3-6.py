#실수 2개를 표준 입력으로 받아 6개의 관계 연산의 결과를 출력하시오.
n1, n2 = input('실수 두 개 입력 >> ').split()
print('{} > {} 결과: {}'.format(n1, n2, n1 > n2))
print('{} >= {} 결과: {}'.format(n1, n2, n1 >= n2))
print('{} < {} 결과: {}'.format(n1, n2, n1 < n2))
print('{} <= {} 결과: {}'.format(n1, n2, n1 <= n2))
print('{} == {} 결과: {}'.format(n1, n2, n1 == n2))
print('{} != {} 결과: {}'.format(n1, n2, n1 != n2))