from datetime import date

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')


f_date = date(int(year),int(month),int(day))
l_date = date(2022, 6, 11)
delta = l_date - f_date

print('\n\n\nToday:',today,'\nLast Day:',l_date,"\n\n\nDays Left:", delta ,'\n\n\n')

credit = input('Credit left:')

print('\n\n\n')

money = float(credit)/delta.days

print('You can use', round(money,2), 'per day.')
