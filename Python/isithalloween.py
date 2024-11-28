month, date = input().split()
date = int(date)

if month == 'OCT' and date == 31:
    print('yup')
elif month == 'DEC' and date == 25:
    print('yup')
else:
    print('nope')