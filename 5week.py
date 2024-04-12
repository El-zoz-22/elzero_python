
#-----------------------------
#week 5 in python 
# ----------------------------

print('\nAssignments For Lessons 33 To 37\n')

print(bool(1))
print(bool("zezo"))
print(bool(True))
print(bool(43))
print(bool(""))
print(bool(None))
print(bool(0))
print(bool({}))

print("*"*25)
#**************************************

html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript >50 )

print("*"*25)
#**************************************

num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


print("*"*25)
#**************************************
num_one = 10
num_two = 20
 
reselt= num_one + num_two
print(reselt)
reselt **= 3
print(reselt)
reselt %=26000
print(reselt)
reselt /= 5
print(reselt)
print(type(str(reselt)))

print("*"*25)
#_______________________________#

print('\nAssignments For Lessons 38 To 40\n')

fname=input("what your name ? ")

fname =fname.strip().capitalize()
print(f"welcom {fname}. how are you ? ")

print("*"*25)
#**************************************

age = int(input("enter your age .."))

if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
elif age >= 16 :
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
    
print("*"*25)
#**************************************
    
fname=input("enter your fname ..") 
lname=input("enter your lname ..")

fname=fname.strip().capitalize()
lname=lname.strip().capitalize()

print(f"Hello {fname} {lname}." )

print("*"*25)
#**************************************

email=input("enter your email..")
email=email.strip().capitalize()

user=email[:email.index('@')].lower()
domain=email[email.index('@') + 1:email.index('.')].capitalize()
Top_Level_Domain=email[email.index('.') +1:]

print(f"Your Name Is {user}")
print(f"Email Service Provider Is {domain}")
print(f"Top Level Domain Is {Top_Level_Domain}")