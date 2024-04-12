#-----------------------------
#week 13 in python 
# ----------------------------




#this is in the web site () >>http


#1)      ([A-z]\s)
######################################
#2)      (L\w{7})
######################################
#3)      (\+?\(\d{4}\)\s\d{2,4}\-\d{4})
######################################
#4)     (https?://(www\.)?\w+\.(org|com)(\:\d{4})?\/(\w+)\.(php|py))
######################################
#5)     https?    [^ab-d]    [th-s]     h\w+    h.+

# this using python
import re

search =re.findall(r"([A-z]\s)","eeeeE llllLl lllzzZzzzz eroe operationr pollo ")
print(search)

######################################
print('*'*25)
search =re.findall(r"(L\w{7})","EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111")
print(search)

######################################
print('*'*25)
search =re.findall(r"(\+?\(\d{4}\)\s\d{2,4}\-\d{4})",
"""+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12""")

print(search)

######################################

print('*'*25)
search =re.findall(r"(https?://(www\.)?\w+\.(org|com)(\:\d{4})?\/(\w+)\.(php|py))",
"""http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net""")

# empty_list=[]
# if search != []:
#     empty_list.append(search)

# print(empty_list)
print(search)

######################################

print('*'*25)
search =re.findall(r"https?|[^ab-d]|[th-s]|h\w+|h.+",
"""http
https
abcd
abcd""")

print(search)