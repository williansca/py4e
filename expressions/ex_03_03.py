score = input('Enter score between 0.0 and 1.0: \n')

try:
    score = float(score)
except:
    print('Error, please enter a numeric input\n')

if score > 1.0:
    print('Invalid number')
    quit()

if score >= 0.9 and score <= 1.0:
    print('A')
elif score >= 0.8 and score <= 0.89:
    print('B')
elif score >= 0.7 and score <= 0.79:
    print('C')
elif score >= 0.6 and score <= 0.69:
    print('D')
else:
    print('F')
