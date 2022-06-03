#한글과 영어에 대응되는 튜플 korean과 english를 만든 후, 표준 입력으로 한글을 입력받아 영어를 출력하시오.

korean=('정렬','초보자','내포','사전')
english=('sorting','novice','comprehension','dictionary')

word=input('찾을 단어 입력? ')
if word in korean:
    print(english[korean.index(word)])
else:
    print('없는 단어 입니다.')
