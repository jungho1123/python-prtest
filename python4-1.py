#월을 표준입력으로 입력받아 계절을 출력하는 프로그램을 작성하시오.
month=int(input('월 입력? '))
if(4<=month<=5):
    print('{}월 봄'.format(month))
elif(6<=month<=8):
    print('{}월 여름'.format(month))
elif(9<=month<=10):
    print('{}월 가을'.format(month))
else:
    print('{}월 겨울'.format(month))