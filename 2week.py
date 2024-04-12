#-----------------------------
#week 2 in python 
# ----------------------------

name='zyad'
age='44'
Country="Egypt"

print(f'''"Hello '{name}', How YOU Doing \ """ ''',F'''Your Age IS "{age}"" + And Your Country Is: {Country}''' )

print('\n','*'*30)
#---------------------------------------------------------------------#

print(f'''"Hello '{name}', How YOU Doing \ \n """ ''',F'''Your Age IS "{age}"" + \n And Your Country Is: {Country}''' )

print('\n','*'*30)
#---------------------------------------------------------------------#

name ='Elzero'
print("",name[1],"\n",name[2],"\n",name[-1])

print('\n','*'*30)
#---------------------------------------------------------------------#

name = 'Elzero'
print("",name[1:4],"\n",name[:5:2],"\n",name[-2::-2])

print('\n','*'*30)
#---------------------------------------------------------------------#

name = "#@#@Elzero#@#@"

print(name.strip('#'+'@'))

print('\n','*'*30)
#---------------------------------------------------------------------#
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print("",num1,"\n",num2,"\n",num3,"\n",num4,"\n",num5,"\n")

print("",num1.zfill(4),"\n",num2.zfill(4),"\n",num3.zfill(4),"\n",num4.zfill(4),"\n",num5.zfill(4),"\n")

print('\n','*'*30)
#---------------------------------------------------------------------#
name_one = "Osama"
name_two = "Osama_Elzero"


print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

print('\n','*'*30)
#---------------------------------------------------------------------#

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

print('\n','*'*30)
#---------------------------------------------------------------------#
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

print('\n','*'*30)
#---------------------------------------------------------------------#
name = "Elzero"

print(name.find("z"))

print('\n','*'*30)
#---------------------------------------------------------------------#
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3","Love",1))

print('\n','*'*30)
#---------------------------------------------------------------------#
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3","Love"))

print('\n','*'*30)
#---------------------------------------------------------------------#
name = "Osama"
age = 38
country = "Egypt"


print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
