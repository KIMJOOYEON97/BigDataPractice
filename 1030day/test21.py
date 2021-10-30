data = [22,45,'B',78.9,'kim',True,16,34,920]

print()
for dt in data:
    print(dt, end = '  ')

#data.remove(45) 데이터값으로 삭제, 없는데이터삭제하면 에러
# del data[3] #3번지의 것이 삭제됌
#del 리스트명[위치] 
del data[1:5] #구간삭제가능
print()
for dt in data:
    print(dt, end = '  ')


print()
data = [22,45,'B',78.9,'kim',True,16,34,920]
del data[3:]
for dt in data:
    print(dt, end = '  ')
print()