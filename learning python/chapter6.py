#loops and iterations

nums = [1, 2, 3, 4, 5]


for num in nums:
    print(num)

#wnat to find a vlue and stop after it, can work indipendentelly without the above 'for'
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#run indipendentelly for better results
for num in nums:
    if num == 2:
        print ('Found!')
        continue
    print(num)

# loop within a loop
mums = [1, 2, 3, 4, 5]

for num in mums:
    for letter in 'abc':
        print (num, letter)

#run through a loop specific times
for i in range (10):
    print(i)

# define running through a loop
for c in range (1, 11):
    print(c)


x = 0
while x < 10:
    print(x)
    x += 1
