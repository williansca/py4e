# Write a program that prompt the user for hours and rate  per hour to compute gross pay


hour = input('Enter Hours: ')
rate = input('Enter Rate: ')

#reg is regular pay
#otp is overtime pay


try:
    fh = float(hour)
    fr = float(rate)
except:
    print('Error, please enter a numeric input')
    quit()
    # quit so the program won't continue

if fh > 40:
    #print('Overtime')
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg, otp)
    xp = reg + otp

else:
    #print('Regular')
    xp = fh * fr

print('Pay:', xp)
