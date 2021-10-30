#test09.py

kor=0;eng=0;hap=0;avg=0
message='메시지'

kor = int(input ("국어점수 >>>"))
eng = int(input("영어점수 >>>"))

print()
hap = kor+ eng
avg = hap/2
message = ''

if avg>=70:
    message = 'pass'
else:
    message = 'Non pass'

print('합계 = ',hap)
print('평균 = ',avg)
print('결과 =',message)
