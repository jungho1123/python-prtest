#다음 리스트와 튜플로 딕셔너리를 만들고 다음과 같이 출력하는 프로그램을 작성하시오.

fruits = ['apple', 'banana', 'grapes', 'pear']
prices = (1000, 500, 1200, 1500)

dictionary = dict(zip(fruits, prices))

print(dictionary)
print()

lst=list(enumerate(dictionary,start=1))

for i in range(len(fruits)):
    print(*lst[i], '가격: {}'.format(prices[i]))
