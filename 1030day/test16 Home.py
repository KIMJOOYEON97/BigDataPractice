
#test16Home.py
# 조건 for 대신 while반복문 사용
# 출력 1 2 3 4 6 7 8 9 10 hap = 50
# 꿀팁 break, continue

su=0;hap=0
while su<10:
    su=su+1
    
    if su == 5:
        continue
    hap= hap+su

    print(su, end=' ')

print('\n합계 = ',hap) 