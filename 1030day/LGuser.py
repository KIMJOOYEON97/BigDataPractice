#사용자입장
import LG

from LG import coffee, dunkin


def game():
    print('LGuser문서 game')
    print('LGuser문서 테란 client_id' ,LG.client_id)
    print('LGuser문서 저그 client_pw' , LG.client_pw)
    print()
    LG.dunkin()
    print()
    LG.coffee()

game()

#함수 안에서만 사용하지 않아도 된다.
print('-'*70)
print('LGuser문서 game')
print('LGuser문서 테란 client_id' ,LG.client_id)
print('LGuser문서 저그 client_pw' , LG.client_pw)
print()
LG.dunkin()
print()
LG.coffee()