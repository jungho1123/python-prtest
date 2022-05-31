#파이썬의 철학을 저장 후 메소드 replace()를 사용해 두 번째 철학으로 다시 저장해 출력하는 프로그램을 작성하시오
str='Beautiful is better than ugly.'
str1=str.replace('Beautiful','Explicit')
str2=str1.replace('ugly','implicit')
print(str2)
