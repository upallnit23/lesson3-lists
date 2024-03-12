#Python Lists Transformation

#Task 1:Grades

grades = [85,90,78,88,76,95,89,80,72,93]

grades.sort()
print (grades)


#Task 2:Calculate the average grade and display it.

sum = 0

for x in range(len(grades)):
    sum += grades[x]
print(sum)

#Task 3:Replace any grade below 80 with the value Failed.

for y in range(len(grades)):
    if grades[y] < 80:
        del grades[y]
        grades.insert(y, "Failed")
    else:
        continue
print(grades)

#Advanced List Methods and Identity Operators

#Given the two lists, find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for x in range(len(submitted)):
    for y in range(len(attended)):
        if submitted[x] == attended[y]:
            print(submitted[x])
        else:
            continue
    
#Task 2:Check if two lists are identical in terms of their content, regardless of order.

count = 0     
for x in range(len(submitted)):
    for y in range(len(attended)):
        if submitted[x] == attended[y]:
            count = count + 1
        else:
            continue

print("There are ", count, " items in both lists that are similar.")

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for x in range(len(submitted)):
    for y in range(len(attended)-1):
        if submitted[x] != attended[y]:
            attended.pop(x) 
        else: 
            continue
print(attended)

#3. Advanced Slicing Techniques

#Task 1:Given the list of temperatures, extract the temperatures for the second week of the month.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

secondweek_temps = slice(7, 14)
print(temperatures[secondweek_temps])

#Task 2:Extract all temperatures above 100.

over100_temps = slice(23, 31)
print(temperatures[over100_temps])

#Task 3:Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

over100_temp = []

for i in range(len(temperatures)):
    if temperatures[i] >= 100:
        over100_temp.append(i)
        #over100_temp.append(i)
    else:
        continue
print(over100_temp)

revtemps = slice(-11,-5)
print(temperatures[revtemps])

#List Comprehensions and Membership Operators

#Task 1:Given the list below, use a list comprehension to create a new list containing only even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = [x for x in range(len(numbers)) if (x % 2 == 0)] 
print(n)

#Task 2:Use a list comprehension to create a new list containing numbers greater than 5.

nlgreaterthan5 = [x for x in range(len(numbers)) if (x >5)]
print(nlgreaterthan5)

original7 = [x for x in range(len(numbers)) if x == 7]
print(original7)

#5. Deep Dive into Python Lists

#Task 1 and 2.  Given list, filter out students who have grades below 80.  Print the name, grade, and activity.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

templist = []

templist.extend(grades)
#print(templist)
templist.extend(students)
templist.extend(activities)
print(templist)

count = 0

for i in range(len(grades)):
    if grades[i] < 80:
        print(grades[i])
    else:
        count += 1
        continue
print(count)

for i in templist:
    templist2 = slice(2, len(templist), (count + 1))
print(templist[templist2])

#Task 3 and 4:For the remaining students, add students to a new list named students_approved, and print the list.

students_approved = []  

for j in templist:
    students_approved.append(j)
for k in students_approved:
    if k == 78:
        students_approved.remove(k)
    elif k == "Jane":
        students_approved.remove(k)
    elif k == "Art":
        students_approved.remove(k)

print(students_approved)















