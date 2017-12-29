#Basic message
message1 = 'Hello World!'

#How to handle quotes in quotes 1
message2 = 'Bobby\'s World!'

#How to handle quotes in quotes 2
message3 = "Bobby\'s World!"

#Multiple Line Script eg:1_three double quotes
message4 = """Multi Line
Script"""

#Multiple Line script eg:2_three single quotes
message5 = '''Multi Line
Script'''

#replacement, how to replace one character with other
message6 = "Hello universe!"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

#length of characters
print(len(message1))

#access characters individually
print(message4[6])

#access first character
print(message1[0])

#access range of characters
print(message1[0:4])

#leave start index blanc, can do for last index too
print(message2[:3])
print(message1[6:])

#printing lower case/upper case
print(message1.lower())
print(message1.upper())

#count takes string as an argument. if want to count strings.
#We have to tell what to count, in the below case Hello or l
print(message1.count('Hello'))
print(message1.count('l'))

#If want to find index where characters are found, world starts at the 6th index of the message variable
print(message1.find('World'))
print(message2.find('Universe'))

#replace characters of the string with other characters, might print just hello world
print(message6)

#how to fix replacement
new_message = message6.replace('Hello', 'Hi')
print(new_message)

#multiple strings
greetings = 'Hello'
name = 'there'
message7 = greetings + name
print(message7)

#How we want message 7
insa = 'Hello'
hae = 'there'
message8 = insa + ', ' + hae + '!'
print(message8)

#formatted string
#message9 = '{}, {}. !'.format(insa, hae)
#print(message9)

#these are f strings
#message10 = f'{greetings}, {name}!'
#print(message10)

#upper or lower with F strings
#message11 = f'{greetings}, {name.upper()}!'
#print(message11)

#attribute and methodes we have access to
#print(dir(name))

#to see what it does, everything is available to us
#print(help(str))

#find out specifically what you want, eg of just what lower does
#print(help(str.lower))
