"""First proper programme
task (1)will input name and age and output will be the year you will turn 100 years old
task (2)input random number and print the above message that many times
task (3)input random number and print the above message that many times in different line"""



#input fields
name = input ('Given Name:')                            #debugging: input field = characters only messages if not
age = int (input('your age:'))
"""if age != (int):
    print ('Numbers only!')"""
year =str((100 - age) + 2017)

#printing
print (name + 'Will be 100 years old in'+ year)        #debugging: spaces needed (task 1 complete)

#number of times you want to see this meassage
x = int(input ('Input random no from 1-9: '))
if x <= 0:
        print('Error: Number too low!')
elif x >= 10:
        print('Error: Number too high!')
else:
    print (year * x)                                    #debugging: spaces and (,) needed (task 2 complete)


                                                        #see the above message in multiple lines
""" Need to learn more - 29:31 (we have values of year and x, but y is just defined
                                but what is nums)
y = {1,2,3}
    for nums in x:
    print (year * nums)
"""

