#-----------------------------
#week 3 in python 
# ----------------------------

print('\nAssignments For Lessons 19 To 20\n')

a=10
print('',int(a))
print("\n",float(a))
print("\n",complex(a))

print("*" * 20)
#*******************************

a=1+2j
print( f"Imaginary Part : {a.imag}")
print(f"Real Par : {a.real}")

print("*" * 20)
#*******************************

num = 10
print("{0:.10f}".format(num))

print("*" * 20)
#*******************************

num = 159.650

num=int(num)
print(num)
print(type(num))

print("*" * 20)
#*******************************

print(100-115)
print(50*30)
print(21%4)
print(110//11)
print(97//20)

print("_" * 20)

#_______________________________#
print('\nAssignments For Lessons 21 To 23\n')

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])

print("*" * 20)
#*******************************

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0:5:2])
print(friends[1:5:2])

print("*" * 20)
#*******************************

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])

print("*" * 20)
#*******************************
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends [3:5]=["Elzero","Elzero"]
print(friends)

print("*" * 20)
#*******************************
friends = ["Osama", "Ahmed", "Sayed"]

friends.append("Salem")

print(friends)

print("*" * 20)
#*******************************
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)

print("*" * 20)
#*******************************
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)

print("*" * 20)
#*******************************
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.reverse()
print(friends)

print("*" * 20)
#*******************************

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

print("*" * 20)
#*******************************
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
print("_" * 20)

#_____________________________________#
print('\nAssignments For Lessons 24 To 25\n')


table = "osama",

print(table[0])
print(type(table))
print("*" * 20)

#*********************************
friends = ("Osama", "Ahmed", "Sayed")
friends=list(friends)
friends[0] = "Elzero"
friends=tuple(friends)
print(friends)
print(type(friends))
print(len(friends),"Element")

print("*" * 20)

#*********************************

nums = (1, 2, 3)
letters = ("A", "B", "C")
new=nums+letters
print(new)
print(len(new)," Elements")

print("*" * 20)

#*********************************
my_tuple = (1, 2, 3, 4)
a,b,_,c=my_tuple
print("",a,"\n",b,"\n",c,"\n")

