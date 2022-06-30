#리스트 sports와 num을 활용해 스포츠 종목과 팀원 수가 번갈아 나오는 리스트를 만든 후 출력하시오

sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]

sports1=sports[:]
sports1.insert(1,num[0])
sports1.insert(3,num[1])
sports1.insert(5,num[2])
sports1.insert(7,num[3])

sports2 = sports[:]
sports2.insert(1,'')
sports2.insert(3,'')
sports2.insert(5,'')
sports2.insert(7,'')

sports3 = sports2[:]
sports3[1::2]=num[:]

print(sports1)
print(sports2)
print(sports3)
