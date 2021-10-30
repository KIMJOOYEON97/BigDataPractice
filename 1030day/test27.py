# 함수 define 리턴값표시없음 함수이름(매개인자):v

#리턴값에 대해 적지 않음 void, int 등

def myname():
    print('고길동')
    print('고희동')

def myCal():
    hap = 90+85
    return hap

def myBitCamp():
    name = 'kim'
    tot = 150
    avg = 78
    return name,tot,avg

#파이썬에서 함수 구현후 반드시 호출
myname()
data = myCal()
print('합계 = ',data)
a,b,c = myBitCamp()
print("이름=",a,"합계 =",b,"평균 =",c)