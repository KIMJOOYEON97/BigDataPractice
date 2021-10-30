
# a=7;b=2;hap=0;cha=0;gob=0;mok=0
# a, b, hap, cha, gob, mok = (5,2,0,0,0,0)
a=7
b=2
hap=0


print('test05.py 2:10')
hap = a+b
print(a,'+',b,'=',hap) #권장
print('%d+%d=%d'%(a,b,hap)) 
print('{}+{}={}'.format(a,b,hap))
print(f'{a}+{b}={hap}') #적극권장
print('-'*70)


# %d형식 %(변수)
# {}  .format()
#f''