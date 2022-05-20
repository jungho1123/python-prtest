#지구를 원이라 가정하고 원둘레를 게산하고 실제와의 차이를 계산하세요
#지구 둘레: 40120km, 반지름은 6378.1km
#원둘레 공식: 2*3.141592*r(반지름)

earth=int(input('지구 둘레'))
r=float(input('반지름'))
dule=2*3.141592*r

print('알려진 지구 둘레:',earth)
print('지구와 같은 원둘레:',dule)
print('차이: {}km'.format(earth-dule))