lst = list('hellopython!')

for i in lst:
    a, b, c = input('슬라이스 [?:?:?] 3개 입력 ').split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0 and b == 0 and c == 0:
        break

    else:
        print(lst[a], lst[b], lst[c])

print('종료'.center(30, '*'))
