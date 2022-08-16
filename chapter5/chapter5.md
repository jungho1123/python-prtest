## 5. 리스트와 튜플

> **리스트**

- 리스트 : 항목의 나열인 시퀀스 (각 항목은 모두 같은 자료형일 필요가 없음)
- 리스트는 [ ] 사이에 항목을 기술
- list.append(삽입할 항목) : 리스트의 가장 뒤에 항목 추가

>
    pl = list()
    pl.append('C++')
    pl.append('Java')
    print(pl)   -> ['C++', 'Java']
    
- len(리스트 이름) : 리스트의 항목 수 출력

>
    py = list('python')
    print(len(py))    -> 6
 
- 리스트 역시 문자열처럼 첨자로 항목 참조 가능  ex) lst[1], lst[2]
- list.count(값) : 값을 갖는 항목의 수 출력
- list.index(값) : 인자의 항목이 위치한 첨자를 반환 

>
    lst = list('hello')
    print(lst.count('l'))   -> 2
    print(lst.index('e'))   -> 1

- 리스트의 항목을 바꾸고 싶다면 첨자로 수정이 가능 

>
    food = ['짜장면', '짬뽕', '우동', '울면']
    food[3] = '탕수육'
    print(food)   -> ['짜장면', '짬뽕', '우동', '탕수육']

- 리스트 슬라이싱 : list[start : end : step]을 통해 리스트 일부 반환 가능
>
    alp = list('abcdefghijk')
    print(alp[0::2])    -> ['a', 'c', 'e', 'g', 'i', 'k']

- list.insert(첨자, 항목) : 리스트의 첨자 위치에 항목을 삽입
>
    py = list('python')
    py.insert(6, '!')
    print(py)   -> ['p', 'y', 't', 'h', 'o', 'n', '!']

- list.remove(항목), pop(첨자) : 리스트에서 지정된 값의 항목 삭제
- list.pop() : 마지막 항목을 삭제하고 삭제된 값을 반환
>
    py = list('python')
    py.pop(4)
    print(py)   -> ['p', 'y', 't', 'h', 'n']
    
    py.remove('y')
    print(py)   -> ['p', 't', 'h', 'n']

- del list[:] : del 뒤에 있는 변수나 항목 삭제, del list는 전부 삭제 가능
>
    py = list('python')
    del py[0]
    print(py)   -> ['y', 't', 'h', 'o', 'n']

    del py[1:3]
    print(py)   -> ['p', 'h', 'o', 'n']

    del py
    print(py)   -> 출력 시 오류 남

- list.clear() : 빈 리스트 출력

- list1.extend(list2),  list1 + list2 : 리스트에 리스트 추가
>
    day1 = ['월', '화', '수']
    day2 = ['목', '금', '토', '일']
    day1.extend(day2)
    print(day1)   -> ['월', '화', '수', '목', '금', '토', '일']

- list.reverse() : 항목 순서를 반대로 바꿈
>
    py = list('python')
    py.reverse()
    print(py)   -> ['n', 'o', 'h', 't', 'y', 'p']

- list.sort() : 리스트 항목의 순서를 오름차순으로 정렬
- list.sort(reverse=True) : 리스트 항목의 순서를 내림차순으로 정렬
- sorted(list) : 항목의 순서를 정렬한 리스트를 반환, 원래의 리스트 자체는 변화 x
- sorted(리스트명,key=lambda x:(int(x[3]),int(x[2]),int(x[1]))) : 리스트를 지정한 항목에 따라 오름차순으로 

<br>
>  **튜플**
