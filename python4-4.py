#인간의 비만도를 측정하는 체질량 지수를 계산해 판정 결과를 출력하세요.
h, w = input('당신의 키와 몸무게는? >> ').split()
height=float(h)
weight=float(w)

bmi=weight/(height/100)**2
print('키: {:.1f}(cm), 몸무게: {:.1f}(kg)'.format(height,weight))

if(40<=bmi):
    print('BMI: {:.1f} {}'.format(bmi,'고도 비만'))
elif(35<=bmi<40):
    print('BMI: {:.1f} {}'.format(bmi,'중등도 비만'))
elif(30<=bmi<35):
    print('BMI: {:.1f} {}'.format(bmi,'비만'))
elif(25<=bmi<30):
    print('BMI: {:.1f} {}'.format(bmi,'과체중'))
elif(18.5<=bmi<25):
    print('BMI: {:.1f} {}'.format(bmi,'정상'))
else:
    print('BMI: {:.1f} {}'.format(bmi, '저체중'))


