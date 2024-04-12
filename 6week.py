#-----------------------------
#week 6 in python 
# ----------------------------

num1=int(input("enter the frist num  "))
 
num2=int(input("enter the second num  "))

operation = input('enter + Or - Or * Or / Or %   ')
if operation == "+" :
    print(f"{num1} {operation} {num2} = ", num1 + num2 )
elif operation == "-" :
    print(f"{num1} {operation} {num2} = ", num1 - num2 )
elif operation == "*" :
    print(f"{num1} {operation} {num2} = ", num1 * num2 )
elif operation == "/" :
    print(f"{num1} {operation} {num2} = ", num1 / num2 )
elif operation == "%" :
    print(f"{num1} {operation} {num2} = ", num1 % num2 )
else:
    print('your data is wrong ' )
    
print("*"*25)
#**************************************
age=int(input('enter your age '))
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

print("*"*25)
#**************************************
age=int(input("enter your age "))
if age < 10 or age > 100 :
    print("the age is not fount in range avalable ")
else:
    print(f"your age by years is {age}")
    print(f"your age by monthes is {age*12}")
    print(f"your age by weeks is {age*12*4}")
    print(f"your age by days is {age*12*4*7}")
    print(f"your age by houer is {age*12*4*7*24}")
    print(f"your age by menetes is {age*12*4*7*24*60}")
    print(f"your age by secondes is {age*12*4*7*24*60*60}")
    
    print("*"*25)
#**************************************
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
country = input("Input Your Country  ").strip().capitalize()
price = 100
discount = 30
print(country)
if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")