#search Arithmetics operations for more
#NO2 - Find data type of objects 'integer'
num = 3
print (type(num))

#Find data type of objects 2 'Float'
num1 = 3.14
print (type(num1))

#Floor division (answer will be only before point)
#in both cases below, seeing single digit; no digit after point
print(float(3) / 2)
print(3 // 2)

#Want to do square operations, 2 times * means power to
print(3 ** 2)

#Modulus operations - gives us remainder after division
print(3 % 2)

#maths is recorded as what learned in schools
print(3 * 2 + 1)
print(3 * (2 +1))

#incrimenting values commonly used ..long way/short wat
one = 1
one = one + 1
print(one)

#Shorter way for printing one = one + 1
Sol = 2
Sol += 2
print(Sol)

#eg 2 for short term incrimenting values
mol = 1
mol *= 10
print (mol)

#built in abs = absolute value; it removes negative sign from any numbers
print (abs(-3))

#round multi digits
james = 3.777
print (round(james))

#define how many you want to round the digits to
print (round(james, 1))

#Comparisons values will output in bulien = true/false values
#Equals             3 == 2      ==
#Not Equal          3 !=2       !=
#Greater than       3 > 2       >
#Less than          3 < 2       <
#Greater or equal   3 >= 2      >=
#Less or Equals     3 <= 2      <=

#comparision, two values are equal, greater etc
num_1 = 3
num_2 = 2
print (num_1 == num_2)
#single = is used as an assignment; == is comparision

print (num_1 != num_2)

print (num_1 > num_2)

print (num_1 < num_2)

print (num_1 >= num_2)

print (num_1 <= num_2)

#some thing looks like a number but its a string..look below
#below are strings but sometimes we might not know
page_1 = '100'
page_2 = '200'
print (page_1 + page_2)

#casting - form string to integers
page_1 = int(page_1)
page_2 = int(page_2)
print (page_1 + page_2)
