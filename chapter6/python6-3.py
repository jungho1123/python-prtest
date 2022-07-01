books={'book1':['writer1'],
       'book2':['writer1','writer2'],
       'book3':['writer1','writer3','writer4']}

for key,values in books.items():
    print('책 이름: {}, 저자: {}'.format(key,values))
