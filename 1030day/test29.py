#파이썬은 튜플 상수 대입후 재할당 불가능 지도에서 위도, 경도

pos =('홍대',31.42538, 129.36491, '홍대') #튜플은 중복이 가능함

for i in range(len(pos)):
    print(pos[i],end="\t")

print()
print('-'*70)
for i,v in enumerate(pos): #enumerate 알아두기
    print(i, ":", v)