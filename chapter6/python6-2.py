#회사 6개의 주식 가격을 딕셔너리로 만든 후 가격 출력

dic={'삼성에스디에스':242000,'삼성전자':47000,'엔씨소프트':52600,'핸디소프트':5120,'골프존':215000,'기아':56300}

while True:
    name=input('주식 이름 ? ')

    if name in dic:
        print('{}: {}'.format(name,dic[name]))

    else:
        print('주식 이름이 없습니다.')
        break
