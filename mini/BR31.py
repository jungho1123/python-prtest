import random

print('베스킨라빈스 게임 시작하겠습니다')
user=['AI','사용자']
br=[]

while True:
    for i in range(len(user)):
        print('{}의 차례입니다'.format(user[i]))
        if user[i]=='사용자':
            x=int(input())
            for i in range(x):
                number=len(br)+1
                br.append(number)
                print(number,end=' ')
                print()
                if number==31:
                    print('사용자 lose'.center(15,'='))
                    break
                number+=1

        else:
            y=random.randint(1,3)
            for i in range(y):
                number2=len(br)+1
                br.append(number2)
                print(number2, end=' ')
                print()
                if number2==31:
                    print()
                    print('AI lose'.center(15,'='))
                    break
                number2 += 1

    if len(br)>30:
        break
