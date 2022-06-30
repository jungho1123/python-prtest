import random

lst = []
for i in range(10):
    a = random.randint(1, 99)
    lst.append(a)

tup = tuple(lst)
stup = sorted(tup)

print('리스트: ', lst)
print('튜플: ', tup)
print('튜플 정렬된 리스트: ', stup)

print('합: {}, 항목수: {}'.format(sum(lst), len(lst)))
print('최대: {}, 최소: {}, 평균: {}'.format(max(lst),min(lst),sum(lst)/10))
