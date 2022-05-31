#한 줄의 문자열을 표준입력으로 받아 범위, 길이, 참조문자를 출력하시오.
str=input('문자열 입력 >> ')
print('참조할 첨자: {}-{}'.format(0,len(str)-1))
num=int(input('참조할 첨자 입력 >> '))
print('문자열: {}, 길이: {}'.format(str,len(str)))
print('참조 문자: {}'.format(str[num]))
