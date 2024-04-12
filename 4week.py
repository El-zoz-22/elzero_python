#-----------------------------
#week 4 in python 
# ----------------------------

print('\nAssignments For Lessons 26 To 32\n')

my_list=[1, 2, 3, 3, 4, 5, 1]
my_list=set(my_list)
unique_list=list(my_list)

print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

print("*" * 20)
#**********************************

nums = {1, 2, 3}
letters = {"A", "B", "C"}


letters.update(nums)

print(letters)
z=nums.union(letters)
print(z)

letters.add(1)
letters.add(2)
letters.add(3)
print(letters)

print("*" * 20)
#**********************************
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.update("B","A")
print(my_set)
my_set.discard("c")

print("*" * 20)
#**********************************
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))


print("*" * 20)
#**********************************


my_dec={
    "HTML":"Progress Is 90%" ,   
    "CSS":"Progress Is 80%",
    "Python":" Progress Is 30%",
}

my_dec.update({"AI":"Progress Is 20%"})
print(my_dec)

print("*" * 20)
#**********************************
