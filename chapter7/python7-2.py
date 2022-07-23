# 복리 계산:복리 총액=원금*(1+이자율기간)

def getinterest(money,rate,year):
    total=300000*(1+rate)**year
    return total

money=300000
rate=0.05
print('예금 원금: 300000')
print('2년 총액: {:.2f}'.format(getinterest(money,rate,2)))
print('4년 총액: {:.2f}'.format(getinterest(money,rate,4)))
print('6년 총액: {:.2f}'.format(getinterest(money,rate,6)))
print('8년 총액: {:.2f}'.format(getinterest(money,rate,8)))
