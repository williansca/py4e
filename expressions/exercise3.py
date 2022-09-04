# Write a program that prompt the user for hours and rate  per hour to compute gross pay

hour = input('Enter Hours: ')
rate = input('Enter Rate: ')
digit = 0

try:
    hour = float(hour)
    rate = float(rate)
except:
    print('Error, please enter a numeric input')
    # quit so the program won't continue
    quit()

if hour <= 40:
    pay = hour * rate
else:
    extra = hour - 40
    hour = 40
    totalExtra = extra * (10 * 1.5)
    pay = hour * 10 + totalExtra
print('Pay:', pay)
