#사용자입장 LGuserBit.py

# from 파일명 as alias
# from 파일명 import 전역변수 함수
from LG import client_id, client_pw, dunkin, coffee

def main():
    print('LGuserBit문서 5:13 5:19 5:25')
    print('LGuserBit문서 client_id' ,client_id)
    print('LGuserBit문서 client_pw' ,client_pw)

    print()
    dunkin()
    print()
    coffee()

#언더바 2개
if __name__ == '__main__':
    print('main이름 명시후 함수 호출')
    main()


