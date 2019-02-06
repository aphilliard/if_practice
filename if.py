while True:
    try:
        a = int(input('Type an integer between 1 and 6: '))
        b = int(input('Type another integer between 1 and 6: '))
        if a not in range(1,7) or b not in range(1,7):
            print("At least one of these is out of range. Try again.")
            continue
    except (ValueError):
        print("Not a number. Try again.")
        continue
    else:
        break

if (6 in (a, b) and a !=6) or (6 in (a, b) and b !=6):
    print('One of these is a 6')
elif (a + b) == 12:
    print('They are both 6')
else:
    print('Neither of these is a 6')
