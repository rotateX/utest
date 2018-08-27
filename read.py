from random import choice
import random

def readcar():
     plates = []
     try:
          with open('E:/pythontest//utest/plateno.txt','r') as data:
               for i in data:
                    plates.append(i.strip())
     except IOError as ioerr:
          print('IOERROR!')
     return(plates.pop(plates.index(random.choice(plates))))


