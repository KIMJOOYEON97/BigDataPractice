#test12.py

kor=0;eng=0;hap=0;avg=0
message='메시지'
grade='학점'
kor = 90 #int(input ("국어점수 >>>"))
eng = 85 #int(input("영어점수 >>>"))

print()
hap = kor+ eng
avg = hap/2
message = ''

#평균 100~90 A, 89~80 B, 79~60 C, 69~60 D, 59~0 F

if avg >= 90:
    grade ='A'
elif avg >= 80:
    grade ='B'
elif avg >= 70:
    grade ='C'
elif avg >= 60:
    grade ='D'
else:
    grade = 'F'
#과목 50점이상 평균70점주터 합격
if (avg>=70):
    message = 'pass'
else:
    message = 'Non pass'

print('합계 = ',hap)
print('평균 = ',avg)
print('학점 =',grade)
print('결과 =',message)
