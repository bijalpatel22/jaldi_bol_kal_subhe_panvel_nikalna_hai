
#lists
courses = ['history', 'math', 'physics', 'compSci']
print(courses)

#check values
print(len(courses))

print(courses[0])

#where 0 is first of total 4, 3 becomes last
print(courses[3])

#negative index = starts from behind
print(courses[-1])

#many values at once same like before
print(courses[0:2])

#if we negate 0, it will consider we start from and end from for last
print(courses[:3])
print(courses[2:])

#list methodes helps to modify lists
#add item to end of list
courses.append('Art')
print(courses)

#add something in specific location
courses.insert(0, 'georaphy')
print(courses)

#find index values
print(courses.index('compSci'))



#2 lists
courses_2 = ['chemistry', 'education']
courses.insert(0, courses_2)
#this will print whole course 2 in courses, not individual value
print(courses)
#how to just add value use extend insted of insert or append
courses_3 = ['hello', 'world']
courses.extend(courses_3)
print(courses)

#remove value
courses.remove('math')
print(courses)
#pop will remove the last value, by default
courses.pop()
print(courses)
#pop is also able to grab the value of what it has popped
popped = courses.pop()

print(popped)

#clean up
courses.reverse()
print(courses)

#sort alp
courses.sort()
print(courses)

nums = [1, 5, 9, 6]
nums.sort()
print(nums)

#desending order    send argument
nums.sort(reverse=True)                 #we are explaining how to sort
print(nums)

sorted(courses)                         #it wont sort and print out but it will sort and save it
print(courses)
sorted_courses = sorted(courses)
print(sorted_courses)


#min, max and sums
print(min(nums))
print(max(nums))
print(sum(nums))

#see if things are in your lists or not
print('Hardik' in courses)

#For loop, looping values               block coding 1st time   we want to create loop where looping through each value and each loop throuh..
for index, item in enumerate (courses):
        print(index, item)


#how to join by commas
morses = ['hindi', 'marathi', 'sanskrit', 'english']
morses_str = ', '.join(morses)          #str is stringing things
print(morses_str)
new_list = morses_str.split(', ')       #now we are splitting stringed and joined things
print(new_list)



#tuples are immutable they cannot be changed/edited like list difference is of brackets
tuple_1 = ('hello', 'world')
tuple_2 = ('hey', 'universe')
print(tuple_1)
print(tuple_2)
tuple_1[0] = 'Art'



        Sets
      #sets are values that are unordered and have no duplicates
      sc_course = {'math', 'math', 'history', 'geograplhy'},
      print(sc_course)      #every time you built this, it will show in different order and also it will not repear math. it got rid of duplicate

