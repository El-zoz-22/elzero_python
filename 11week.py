
#-----------------------------
#week 11 in python 
# ----------------------------

import random 
#import sys
#print(sys.path)
#print(dir(random))

print(f"Random Number Between 10 And 50 => {random.randint(10,50)} ")

eve= random.randint(2,10)
if eve%2 ==0:
   print(f"Random Even Number Between 2 And 10 => {eve} ")
else:
    print(f"Random Even Number Between 2 And 10 => {eve+1}")

od=random.randint(1,9)
if od % 2 != 0:
    print(f"Random Even Number Between 2 And 10 => {od} ")
else:
    print(f"Random Even Number Between 2 And 10 => {od+1} ")
     
#**************************************
print("*"*25)

print(dir(random))


import pyfiglet
print(pyfiglet.figlet_format("el-zoz"))


#**************************************
#_____________________________________
print("*"*25)


import datetime
print(dir(datetime.datetime))
date =datetime.datetime(2021,6,25)
now =datetime.datetime.now()
print(f"Days From {date} To {now} Is => {((now - date).days)}")
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%b %d, %Y"))
print(now.strftime("%d - %b - %Y"))
print(now.strftime("%d / %b / %y"))
print(now.strftime("%d / %B / %Y"))
print(now.strftime("%a ,%d %B %Y"))
#_______________________________________

print('_'*25)

def reverse_string(my_string):
    for item in reversed(my_string):
        yield item 


for c in reverse_string("Elzero"):
    print(c , end='')

print('\n')

#*************************************
print("*"*25)


def frefunc(func):
   
   def sonfunc():
      
      print('Sugar Added From Decorators')

      func()

      print('####################') 
   return sonfunc


@frefunc
def make_tea():
  print("Tea Created")

@frefunc
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
