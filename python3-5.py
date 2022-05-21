#시각 정보를 표준입력으로 받아 다시 시, 분, 초로 출력하는 프로그램을 작성하시오.
time=input('시각 정보 입력 >> ')
hours, mins, secs = time.split(':')
print('{}시 {}분 {}초'.format(hours,mins,secs))

