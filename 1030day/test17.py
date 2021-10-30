msg = 1234
print(msg)
print('|{}|'.format(msg))
print('|{:^10}|'.format(msg)) # 중잉정렬
print('|{:>10}|'.format(msg)) # >오른쪽정렬
print('|{:<10}|'.format(msg)) # <왼쪽정렬
print()