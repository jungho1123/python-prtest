#근로 시급 12000, 일주일에 40시간 이상 근무 시 시급 1.5배, 근로시간은 35~50시간 -> 주급을 계산해 5번 출력하시오.
import random

pay=12000
for i in range(5):
    worktime = random.randint(35, 51)
    if(worktime<40):
        print('근로 시간 {}시간, 주급 {}'.format(worktime, worktime*pay))
    elif(worktime>=40):
        print('근로 시간 {}시간, 주급 {}'.format(worktime, ((worktime-40)*1.5*pay)+40*pay))
    else:
        print()
