a = int(input('Type an integer: '))
b = int(input('Type another integer: '))

if (6 in (a, b) and a !=6) or (6 in (a, b) and b !=6):
    print('One of these is a 6')
elif (a + b) == 12:
    print('They are both 6')
else:
    print('Neither of these is a 6')
