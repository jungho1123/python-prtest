korean=('정렬','초보자','내포','사전')
english=('sorting','novice','comprehension','dictionary')

word=input('찾을 단어 입력? ')
if word in korean:
    print(english[korean.index(word)])
else:
    print('없는 단어 입니다.')
