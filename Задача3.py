x = int(input())
if x % 5 != 0 and x % 7 != 0:
    print('00')
elif x % 5 == 0 and x % 7 != 0:
    print('01')
elif x % 5 != 0 and x % 7 == 0:
    print('10')
elif x % 5 == 0 and x % 7 == 0:
    print('11')
