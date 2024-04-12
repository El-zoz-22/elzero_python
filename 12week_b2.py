NUM = input("Add Your Number ")
if len(NUM)>1:
    raise IndexError('Only One Character Allowed')
NUM=int(NUM)
if NUM<=0:
    raise ValueError('Number Must Be Larger Than 0')
if NUM>9:
    raise Exception('Only Numbers Allowed')

print('############')
print(NUM)
print('############')

#######################################
print(25*'#')

try:
     LETTER = input("Add Letter From A to Z ")
     if len(LETTER) != 1:
        raise ValueError("You Must Write One Character Only")
     if not ('A' <= LETTER <='Z' ):
        raise ValueError("The Letter Not In A - Z")
except ValueError as vs:
   print(f'error: {vs}')
  
else:
   print(f"You Typed {LETTER}")
  

#######################################
print(25*'#')

def calculate(num1, num2) -> int:
  return num1 + num2

print(calculate(20, 30))