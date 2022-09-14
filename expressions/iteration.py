n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
#print(n)

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

friends = ['Joseph', 'Gleen', 'Sally']
for friend in friends:
    print('Happy new year:', friend)
print('Done')

total = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    n = number
    total = total + n
    print(total)

biggernumber = -1
arrayNumber = [10, 50, 5, 3, 88, 90, 200, 1, 0, 33]

for num in arrayNumber:
    if biggernumber < num:
        biggernumber = num
    print('Largest so far', biggernumber)

print('Largest number is', biggernumber)


def bigger(thelist):
    bignumber = -1
    for num in thelist:
        if bignumber < num:
            bignumber = num
    print('Largest so far', bignumber)
    return bignumber


array = [10, 50, 5, 3, 88, 90, 200, 1, 0, 400]
bigger(array)
