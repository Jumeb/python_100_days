year = int(input('Which year do you want to check? '))

if year % 400 == 0:
    if year % 4 == 0:
        print('The year is a leap year')
else:
    print('The year is not a leap year')