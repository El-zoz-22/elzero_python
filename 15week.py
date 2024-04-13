#-----------------------------
#week 15 in python 
# ----------------------------

import sqlite3

db = sqlite3.connect("1.db")

cr = db.cursor()
#cr.execute("CREATE TABLE if not exists users (user_id integer, name text)")

cr.execute("CREATE TABLE if not exists skills (name text, progress integer,user_id integer,age float,email srings,gender boolean,date  Date)")

#=====> name Text,user_id integer,age float,email Strings ,gender Boolean ,date  Date/Time

db.commit()

db.close

###########################################
print('*'*25)


import sqlite3
db = sqlite3.connect("elzero.db")

cr = db.cursor()

cr.execute("CREATE TABLE if not exists users (id integer UNIQUE,name text UNIQUE,dob text UNIQUE,email text)")

# try:
#     cr.execute("INSERT into users(id,name,dob,email) values(1,'Ahmed','20/10/1980', 'a@elzero.org')")
#     cr.execute("INSERT into users(id,name,dob,email) values(2,'Sayed','20/10/1990', 's@elzero.org')")
#     cr.execute("INSERT into users(id,name,dob,email) values(3,'Gamal','20/10/1991', 'g@elzero.org')")
#     cr.execute("INSERT into users(id,name,dob,email) values(4,'Mahmoud','20/10/1987', 'm@elzero.org')")
#     cr.execute("INSERT into users(id,name,dob,email) values(5,'Sameh','20/10/2000', 's@elzero.org')")

num=[1,2,3,4,5]
names=['Ahmed','Sayed','Gamal','Mahmoud','Sameh']
date=['20/10/1980','20/10/1990','20/10/1991','20/10/1987','20/10/2000']
emails=['a@elzero.org','s@elzero.org','g@elzero.org','m@elzero.org','s@elzero.org']

for i in range(len(num)):
    try:
        cr.execute(f"INSERT into users(id,name,dob,email) values({num[i]},'{names[i]}','{date[i]}','{emails[i]}')")
    except:
        print("the date is exists")
        
db.commit()

###########################################
print('*'*25)

# cr.execute("SELECT * FROM users WHERE id = 5")
cr.execute("SELECT * FROM users")
row = cr.fetchall()

print(row[-1])
db.commit()

###########################################
print('*'*25)

user_id=input("enter your num ID ").strip()
cr.execute(f"SELECT id FROM users where id ='{user_id}'")
use = cr.fetchone()
if use != None:
    cr.execute(f"delete from users where id='{user_id}'")
    
    print("User Deleted.")
    print("Show Other Data:")
    
    cr.execute(f"select * from users")
    reselts=cr.fetchall()
    
    for row in reselts:
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")
        

        
else:
    print("User Not Found.")
    


# except sqlite3.IntegrityError as e:
#     print(f"Error: {e}")

# cr.execute("select * from users where id=5")

db.commit()
db.close()