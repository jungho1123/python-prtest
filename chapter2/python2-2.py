#킬로미터 단위로 거리를 입력받아 마일(mile) 단위로 변환해 출력
#1mile=1.61km
km=int(input('차의 속도를 입력(km) >> '))
mile=float(input('마일'))   #1.61입력
print('{}(km)은 {} 마일(miles)이다.'.format(km,km/mile))
