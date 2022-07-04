## 6. 딕셔너리와 집합

> **딕셔너리**

- **딕셔너리(dict())** : 키와 값의 쌍인 항목을 나열한 시퀀스 
- 항목 순서에는 의미가 없으며, 키는 중복 불가능
- 키는 수정 불가능, but 값은 수정 가능

>
    month = {1: 'january', 2: 'febrary', 3: 'march', 4: 'april'}
    month[5] = 'may'
    print(month)    
    -> {1: 'january', 2: 'febrary', 3: 'march', 4: 'april', 5: 'may'}

- **keys()** : 키로만 구성된 리스트 반환 

>
      month = {1: 'january', 2: 'febrary', 3: 'march', 4: 'april'}
      print(month.keys())   
      -> dict_keys([1, 2, 3, 4])
 
- **items()** : (키, 값) 쌍의 튜플이 들어있는 리스트 반환

>
    month = {1: 'january', 2: 'febrary', 3: 'march', 4: 'april'}
    print(month.items())
    -> dict_items([(1, 'january'), (2, 'febrary'), (3, 'march'), (4, 'april')])

- **values()** : 값으로 구성된 리스트 반환

>
    month = {1: 'january', 2: 'febrary', 3: 'march', 4: 'april'}
    print(month.values())
    -> dict_values(['january', 'febrary', 'march', 'april'])
