"""
문제1. 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
...
ZABCDEFGHIJKLMNOPQRSTUVWXY

문제2.
    *
   ***
  *****
 *******
*********
"""


#문제2
for i in range(1,6):
    for j in range(1,2*i):
        print("*", end="")
    print()


#문제1
k=ord('A')
for i in range(0,26):
    k+=i
    for j in range(0,26): 
        print(chr(k+j), end="")
    print()



