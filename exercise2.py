""" Algorithmic exercise
    (1) Ask user to input random number, depending on the input data give reply
    (2) Different messages for odd and even
    (3) Special message for multiples of 4
    (4) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

No = int(input('Give me a number: '))
if No %2 == 0:
    print ('Your number is even!')
else:
    print ('Your number is odd!')

if No %4 == 0:
    print ('Lucky number!')

str_1 = int(input('Another numerator: '))
str_2 = int(input('Last denomiator: '))
numerator = int(float(str_1))
denomiator = int(float(str_2))
if denomiator == 0:
    print ('Cannot accept 0 as denomiator. Peace out!')
    sys.exit()
else:
    if numerator % denomiator == 0:
        print ('{} divides evenly into {}'. format (denomiator, numerator))
    else:
        print ('{} does not divide evenly into {}'. format (denomiator, numerator))


