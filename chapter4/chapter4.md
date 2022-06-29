## 4. 조건과 반복

> **if ... else**

- **if** : 조건에 따라 해야 할 문장들을 처리해야 하는 경우에 사용 
>
      height = 152
      if 140<=height:
          print('통과')
<br>

- **if ... elif** : 조건의 여러 경로 중 하나를 선택
>
      pm = float(input('미세먼지 농도는? '))

      if 151<=pm:
          print('미세먼지 농도 : {}'.format('매우 나쁨'))

      elif 81<=pm:
          print('미세먼지 농도 : {}'.format('매우 나쁨'))

      elif 31<=pm:
          print('미세먼지 농도 : {}'.format('매우 나쁨'))

      else:
          print('미세먼지 농도 : {}'.format('매우 나쁨'))
<br>

> **for, while**

- **for** : 정해져 있는 시퀀스의 항목 값으로 반복을 실행

>
     sum = 0

     for i in 1.1, 2.5, 3.6, 4.2, 5.4:
         sum+=i
         print(i,sum)

     else:
          print('합: {:2f}, 평균: {:.2f}'.format(sum,sum/5))
<br>

- **while** : 횟수를 정해놓지 않고 어떤 조건이 False가 될 때까지 반복을 수행하는 데 적합

>
     max=4
     cnt=0
     
     while True:
         height=float(input('키는? '))
         if height<130:
             cnt+=1
             print('입장 가능')

         else:
             print('입장 불가능')

        if cnt==max:
             print('다음에 이용해 주세요')
             break
<br>

> **break, continue**  
- **break** : 반복을 종료 (반복 종료 후 반복 문장 이후를 실행)

>
     while True:
         menu=input('0 or 1? ')
         if menu=='0':
             break

     print('종료')
<br>

- **continue** : continue 이후의 문장을 제외하고 계속 반복

>
     for s in 'python':
         if s in 'aeiou':
             continue
         print(s,end=' ')

     else:
         print()
<br>
     
