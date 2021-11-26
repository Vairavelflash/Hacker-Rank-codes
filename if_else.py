# my code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0:
        print('Weird')
   
    else:
     if (n>2) & (n<5):
         print('Not Weird')
     elif(n>6) & (n<20):
        print('Weird')
     elif(n>20):
         print('Not Weird')
        

# standard code
import sys

n = int(input())
if n%2==1 or n in range (5,21):
    print("Weird")
else:
    print("Not Weird")