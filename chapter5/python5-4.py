#각 행의 합과 열의 합을 리스트 rsum과 csum에 저장해 출력하시오

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

rsum=[data[0][0]+data[0][1]+data[0][2],data[1][0]+data[1][1]+data[1][2],data[2][0]+data[2][1]+data[2][2]]
csum=[data[0][0]+data[1][0]+data[2][0],data[0][1]+data[1][1]+data[2][1],data[0][2]+data[1][2]+data[2][2]]

print('각 행의 합: ', rsum)
print('각 열의 합: ', csum)
