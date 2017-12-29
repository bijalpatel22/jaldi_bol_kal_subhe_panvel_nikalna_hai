#dictionary
student = {'name': 'John', 'age': 23, 'courses' : ['math', 'compSci'], 'class': 'of 2013', 'mom': 'problem'}
print(student)
print(student['courses'])
print(student['name'])

#this will show an KEY error
#print(student['phone'])

print(student.get('phone')) #this will show - none as there is no phone string in dictionary
print(student.get('phone', 'Not Found!'))   #now insted of none it will say not found!

#dictionaries can be updated
student['name'] = 'Jane'
print(student)

#update via update methode
student.update({'name': 'Bane', 'age': '99'})
print(student)

#delete dictionary data
del student['age']
print(student)

#another methode to delete
courses = student.pop('courses')
print(courses)

#loop thorugh - length
print(len(student))
#keys
print(student.keys())   #courses and age is removed see above
#values
print(student.values())
#keys and vlues
print(student.items())

for key in student:
    print(key)

for key, values in student.items():
    print(key, values)

