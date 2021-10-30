
#test14for.py


#파이썬에서 반복문 for
# for 대표변수 in rang(1,10,1씩증분 생략가능): #9회 10앞에까지
#   반복처리문장

# for 대표변수 in rang(10): #0~9회까지 10회
#   반복처리문장

# for 대표변수 문자열/리스트/튜블/딕션: #9회 10앞에까지
#   반복처리문장

#파이썬에서 반복문 while
# cnt = 0
#while True:
#   cnt = cnt + 1
#   처리  
#   if cnt==10:
#       break 

# cnt = 0
#while cnt<10:
#   cnt = cnt + 1
#   처리  

for row in range(1,10,1):
    # print(row) #9번처리가 라인 개행
    print(row, end ='\t') #9번처리가 라인 개행대신 tab

print()
su = 0
for k in range(1,10):
    su = su+1
    print(su, end='\t')


