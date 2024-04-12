
#-----------------------------
#week 12 p1 in python 
# ----------------------------


my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):

  # Write Your Code Here
    my_data.extend(data)
    final_string= (''.join(my_data)).capitalize() 
    
print(final_string) # Elzero

###########################################
print('*'*25)


my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    item1=str(item1)
    my_data.extend(item1)
    if (len(my_data)) == (len('Elzero')):
        final_string= (''.join((my_data))).capitalize()

print(final_string)

###########################################
print('*'*25)

from PIL import Image
img = Image.open(r"C:\Users\z\Pictures\elzero-pillow.png")
img.show()
mybox=(400,0,800,400)
newimg=img.crop(mybox)
newimg = newimg.convert('L')
newimg.show()

mybox2=(0,400,1200,800)
newimg2=img.crop(mybox2)
newimg2 = newimg2.convert('L')
newimg2 = newimg2.rotate(180)

newimg2.show()

###########################################
print('*'*25)
"""
this is document fotr this funnc
mkmsvsm dkmmpmv  kmfwmwrkmp
oldokko dcodmdo ekdsmk
"""
def say_hello_to(name):
     """
     parameter(someone) => Person Name
     Function To Say Hello To Anyone
     """

     msg='Hello'
     return f'{msg} {name}'

print(say_hello_to("Osama"))
print(say_hello_to.__doc__)

###########################################
print('*'*25)

#in this task you should change name of file ^_^
"""
This module contains a function for greeting friends.
"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> None:
    """
    This is a description for our task for Elzero Python.
    """
    for someone in some_people:
        print(f"Hello {someone}")

say_hello(my_friends)
print()