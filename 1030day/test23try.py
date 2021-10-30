a=7;b=5;hap=0;mok=0
try:
    hap=a+b
    mok=a/b #여기 연산에러 발생
except:
    # print('오류로 인해 정확한 결과가 아닙니다.')
    # pass
    None

print(f'{a}+{b}={hap}')
print(f'{a}/{b}={round(mok,2)}')

print()
print('승인 필수 공공데이터활용')
print('확인 필수 data.go.kr사이트가입')
print()
