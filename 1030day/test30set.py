#파이썬은 튜플 상수 대입후 재할당 불가능 지도에서 위도, 경도

pos =('홍대',31.42538, 129.36491, '홍대') #튜플은 중복이 가능함
wish = {'bc',2400,'blue','3700','bc','3700','bc'} #set 중복 허용 X, 순서가 없음



#리스트는 추가함수 append(), insert(순서, 데이터)
#튜플은 추가안됨
#셋은 추가가능함  그런데 add
wish.add("그램")
wish.add("LG")

for i in wish:
    print(i,end=" ")
print()


#set를 리스트화 list
#print(), int() , input(), float(), round(), append(), insert(1,2), list()
page = list(wish)
