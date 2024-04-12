
#-----------------------------
#week 7 in python 
# ----------------------------

num = int(input("enter the numper "))
z=0
while num > 0 :
    num -=1
    if num == 6:
        continue
    if num == 0:
        break
    print(num)
    z+=1

else:
    print("Number 0 Is Not Larger Than 0")
print(f"{z} Numbers Printed Successfully.") 
   
print("*"*25)
#**************************************

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
l=0
a = 0
while a < len(friends):
    if friends[a][0].islower(): 
        l += 1
    else:
        print(friends[a])
    a += 1
print(f'Friends Printed And Ignored Names Count Is {l}')

print("*"*25)
#**************************************

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

    print(skills.pop(0))
    
print("*"*25)
#**************************************

frindes = []
lemet=4

while len(frindes) < 4:
    name=input("enter the name ").strip()
    
    if name.islower():
        frindes.append(name.capitalize())
        lemet -= 1
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {lemet}")
     
    elif  name.isupper():
        print("Invalid Name")
        continue

    elif name[0].isupper():
        frindes.append(name)
        print(f"Friend {name} Added")
        lemet -= 1
        print(f"Names Left in List Is {lemet}")
    else:
        break
    
while frindes:
    print(frindes.pop(0))
   
print("*"*25)
#**************************************

#_______________________________#

print('\nAssignments For Lessons 51 To 55\n')

my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort()
my_nums.reverse()
z=0
for n in my_nums:
    if n % 5 == 0 :
        z += 1
        print(f"{z} => {int(n)}")  
print("All Numbers Printed") 

print("*"*25)
#**************************************

for i in range(1,21):
    
    if i == 6 or i == 12 or i == 8 :
        continue
    else:
        print(str(i).zfill(2)) 
print("All Numbers Printed")
    
print("*"*25)
#**************************************
    
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
z=0
for l , d in my_ranks.items():
    if d == "A":
        z += 100
        print(f"My Rank in {l} Is {d} And This Equal 100 Points")
    elif d == "B":
        z += 80
        print(f"My Rank in {l} Is {d} And This Equal 80  Points")
    elif d == "C":
        z += 40
        print(f"My Rank in {l} Is {d} And This Equal 40  Points")
print(f"Total Points Is {z}")

print("*"*25)
#**************************************

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for name in students:
    z=0
    print("------------------------------")
    print(f"-- Student Name => {name}")
    print("------------------------------")
    for sub in students[name]:
        
        if students[name][sub] == "A":
            z += 100
            print(f"- {sub} => 100 Points")
        elif students[name][sub] == "B":
            z += 80
            print(f"- {sub} => 80 Points")
        elif students[name][sub] == "C":
            z += 40
            print(f"- {sub} => 40 Points")
        elif students[name][sub] == "D":
            z += 20
            print(f"- {sub} => 20 Points")
    print(f"Total Points For Sayed Is {z}")

