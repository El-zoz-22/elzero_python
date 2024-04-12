#-----------------------------
#week 8 in python 
# ----------------------------

def calculate(num1,num2,opr="add"):
    opr=opr.strip()
    opr=opr.lower()
    if opr == "add" or opr == "a":
        print(num1+num2)
    elif opr == "subtract" or opr == "s":
        print(num1-num2)
    elif opr == "multiply" or opr == "m":
        print(num1*num2)    



calculate(10, 20) # 30
calculate(10, 20, "AdD") # 30
calculate(10, 20, "a") # 30
calculate(10, 20, "A") # 30
calculate(10, 20, "S") # -10
calculate(10, 20, "subTRACT") # -10
calculate(10, 20, "Multiply") # 200
calculate(10, 20, "m") # 200

print("*"*25)
#**************************************
def addition(*nums):
    z=-5
    c=0
    a=0
    for n in nums:
        if n == 10:
            continue
        else:
            if n == 5 :
                a += z  
            else:      
                c += n
    print(c+a) 

addition(60, 10, 10, 5, 10)
addition(10, 20, 30, 10, 15, 5, 100)
addition(10, 20, 30, 10, 15)



print("*"*25)
#**************************************

def show_skills(name,*skill ):
    
    if skill:
        print(f"Hello {name} Your Skills Is")
    
        for sk in skill :
            print(f"- {sk}")
    else:
        print(f"Hello {name} You Have No Skills To Show")
    
    
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print("*"*25)
#**************************************

def say_hello(name="unknown",age="unknown",country="unknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")
    
    
    
say_hello("Osama", 38, "Egypt")
say_hello()

print("*"*25)
#_______________________________#

print('\nAssignments For Lessons 60 To 64\n')

def get_score(**skills):
    for name,degry in skills.items():
        print(f"{name} => {degry}")
        
get_score(Math=97, Science=80,)

print("*"*25)
#**************************************
def get_people_scores(user=False,**skills):
    if skills:
        if user:
            print(f"Hello {user} This Is Your Score Table:")
            
        for Name,degry in skills.items():
            print(f"{Name} => {degry}")
    else:
        print(f"Hello {user} You Have No Scores To Show")

get_people_scores('ALi', Logic=70, Problems=60)
print("*"*25)
#**************************************
scores_list={
"Math":90,
"Science":80,
"Language":70
}
def get_the_scores(user=False,**skils):
    if skils:
        if user:
            print(f"Hello {user} This Is Your Score Table:")
            
        for Name,degry in skils.items():
            print(f"{Name} => {degry}")
    else:
        print(f"Hello {user} You Have No Scores To Show")
    
    
get_the_scores("Osama")