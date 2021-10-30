#파이썬은 튜플 상수 대입후 재할당 불가능 지도에서 위도, 경도

#pos =['신촌',37.42538, 126.36491] #리스트
pos =('홍대',31.42538, 129.36491) #튜플
print(pos[0])
print(pos[1])
print(pos[2])
pos[0]='선유도' #TypeError: 'tuple' object does not support item assignment
print(pos[0])
# pos.insert(1, 76.03421)
# print(pos[1])