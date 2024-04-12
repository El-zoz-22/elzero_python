#-----------------------------
#week 10 in python 
# ----------------------------

print('\nAssignments For Lessons 69 To 71\n')

from functools import reduce


values = (0, 1, 2) 

if any(values): # if any valy is true do it  

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): #if any condetion is true print good el print bad

  print("Good")

else:

  print("Bad")

print("*"*25)
#**************************************

v=40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print("*"*25)
#**************************************

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")
  
print("*"*25)
#**************************************
  
  
def my_all(x):
    for z in x:
      if z : 
        a='true'
        continue
      else:
        a='false'  
    print(a)
  
my_all([1, 2, 3])
my_all([1, 2, 3, []])
  
  
print("*"*25)
#************************************** 
  
  
def my_any(x):
    for z in x:
      if z : 
        a='true'
        break
      else:
        a='false'  
    print(a)
  
my_any([0, 1, [], False])
my_any([(), 0, False])

print("*"*25)
#**************************************
  
def my_min(x):
  mine = x[0]
  for z in x:
    if z < mine:
      mine = z
      
  print(mine)
  
my_min([10, 100, -20, -100, 50])
my_min((10, 100, -20, -100, 50))

print("*"*25)
#**************************************

def my_max(x):
  maxe = x[0]
  for z in x:
    if z > maxe:
      maxe = z
      
  print(maxe)
  
my_max([800, 100, -20, -100, 50, 700])
my_max((10, 100, -20, -100, 50, 700))

print("_"*25)
#______________________________________________
print('\nAssignments For Lessons 72 To 75\n')   


def remove_chars(cleaned_list ):
 for o in cleaned_list :
  
  return cleaned_list [1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list =map(remove_chars,friends_map)
for z in cleaned_list :
  print(z)

print("__________________another___________________")

#______________________________________________
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
for z in  map(lambda cleaned_list:cleaned_list[1:-1]   ,friends_map):
  print(z)


print("*"*25)
#**************************************  

def get_names(names):
  if names.endswith("m"):
    return names
  
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names,friends_filter)
for b in names:
  print(b)
  
print("__________________another___________________")
#______________________________________________

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

for b in filter(lambda names : names.endswith("m") ,friends_filter):
  print(b)
  
print("*"*25)
#************************************** 

def sum(num1,num2):
  return num1 * num2
nums = [2, 4, 6, 2,]
result = reduce(sum,nums)
print(result)

print("__________________another___________________")
#______________________________________________

nums = [2, 4, 6, 2,]
result = reduce(lambda num1,num2 :num1 * num2 ,nums)
print(result)

print("*"*25)
#************************************** 


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills=list(skills)
skills.reverse()

result_skill= enumerate(skills,50)
for c,s in result_skill:
  s=str(s)
  if s.isdigit():
    continue
  else:
    print(f"{c} - {s}")
    

print("__________________another___________________")
#______________________________________________
    
data = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = 50
i=50

z = len(data) + index - 1
while z >= index:
    item = data[z - index]
    if not isinstance(item, int):
        print(f"{i} - {item}")
        i +=1   
    z -= 1
