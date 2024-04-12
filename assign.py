#-----------------------------
#week 9 in python 
# ----------------------------
#C:\Users\zz\Desktop\python #
#wher i save my code

import os

print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))

#os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_name = (os.getcwd())
file_name = file_name[::-1]
file_name = file_name[:file_name.index("\\")]
file_name = file_name[::-1]
print(file_name)

file_name = (os.path.dirname(__file__))
file_name = file_name[::-1]
file_name = file_name[:file_name.index("\\")]
file_name = file_name[::-1]
print(file_name)

file_name = (os.path.abspath(__file__))
file_name = file_name[::-1]
file_name = file_name[:file_name.index("\\")]
file_name = file_name[::-1]
print(file_name)

file_num =1
for i in range(1,51):
    if i == 25:
        file_25 = open(fr"C:\Users\z\Desktop\python\special-text","w")
        file_25.close()
    else:
        myfile=open(fr"C:\Users\z\Desktop\python\txt{i}.txt","w")
        myfile.write(f"Elzero Web School=>{i}\n")
        myfile.close()
    file_num += 1
    
#******************************
print("*"*25)

myfile=open(r"C:\Users\z\Desktop\python\txt1.txt","a")
myfile.write("Appended=>Elzero Web School\n"*50)
myfile.close()

#******************************
print("*"*25)

final_file = open(r"C:\Users\z\Desktop\python\txt1.txt","r")
file_list = final_file.readlines()
num_line = len(file_list)
num_word = 0
num_ch = 0
num_ch_l = 0

for a in file_list:
    b = a.split()
    num_word += len(b)
    for c in a:
        z = c.strip()
        num_ch += len(z)
        num_ch_l += c.count("l")      
        
print(f"Number Of Lines Is => {num_line}")
print(f"Number Of Words Is => {num_word}")
print(f"Number Of Chars Is => {num_ch}")
print(f"Number Of 'l' Char Is => {num_ch_l}")
myfile.close()


#******************************
print("*"*25)

for x in range(41,51):
    
    os.remove(fr"C:\Users\z\Desktop\python\txt{x}.txt")




