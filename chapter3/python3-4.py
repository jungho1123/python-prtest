#find(), 문자열 슬라이싱을 활용해 부분 문자열을 작성하세요
url='https://docs.python.org/3/tutorial'
print(url[:url.find('://')])
print(url[url.find('docs'):url.find('/3/')])
print(url[url.find('tutorial'):])
