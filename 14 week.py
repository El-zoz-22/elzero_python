class student:
    def __init__(self,fname,lname,gender):
        self.fname=fname
        self.lname=lname
        self.gender=gender

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def name_with_title(self):
        if (self.gender == "male"):
            return f" HI MR {self.fname}"
        elif (self.gender == "female"):
            return f"HI MISS {self.fname}"
        else:
            return f"HI {self.fname}"
        
    def all_data(self):
        return f"{self.name_with_title()}\n is not it : {self.full_name()} ?"
        
    
s1=student("zyad","mohamed","male")
s2=student("ali","momen","male")
s3=student("hafsa","elkholey","female")

print(s1.all_data())
print()
print(s3.all_data())

class Game:
    def __init__(self,name,dev,time,price):
        self.name=name
        self.developer=dev
        self.year=time
        self.price=price
    def price_in_pounds(self):
       p=(15*self.price)
       return f"{float(p)} Egyptian Pounds"
        
game_one = Game("Ys", "Falcom", 2010, 50)
print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 750.0 Egyptian Pounds"



class User:
    
  # Write Class Content
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
      
    def full_details(self):
        if self.gender =="Male":
            return f"Hello Mr {self.fname} M. [{40-self.age}] Years To Reach 40"
        elif self.gender =="Female":
            return f"Hello Mrs {self.fname} O. [{40-self.age}] Years To Reach 40"
      
    
        
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

class Message:
  # Write Class Content
  @classmethod
  def print_message(cls):
      return f"Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message

class Games:
  
  # Write Class Content
  def __init__(self,name):
    self.name = name
    
  def show_games(self):
    if self.name == str :
      return f"I Have One Game Called {self.name}"
    elif self.name == list:
      return f"I Have Many Games: {self.name}"
    elif self.name == int:
      return f"I Have {self.name} Game."

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()

my_games_names.show_games()

my_games_count.show_games()

class Games:
    def __init__(self, name):
        self.name = name
    
    def show_games(self):
        if isinstance(self.name, str):
            return f"I Have One Game Called {self.name}\n"
          
        elif isinstance(self.name, list):
            print(f"I Have Many Games:")
            games=''
            for i in (self.name):
              games += f"-- {i}\n"
            return games
          
        elif isinstance(self.name, int):
            return f"I Have {self.name} Game."

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

print(my_game.show_games())
print(my_games_names.show_games())
print(my_games_count.show_games())



# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
  def __init__(self, n, p):
    Members.__init__(self, n, p)
    
# Create Moderators Class Here
class Moderators(Members):
  def __init__(self, n, p):
    super().__init__(n, p)

    
 
member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator


class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

# Write The Class Called "Name" Here
class Text(A,B,C):
  def __init__(self,one,tow,three):
   A.__init__(self,one)
   B.__init__(self,tow)
   C.__init__(self,three)
   
  def show_name(self):
    return f"The Name Is {self.one}{self.two}{self.three}"
  

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero


