import time
import random
import newplateno
from log import logger


#车牌读取
def readcar():
     plates = []
     try:
          with open('E:\pythontest\\utest\plateno.txt','r') as data:
               for i in data:
                    plates.append(i.strip())
          
          return(plates.pop(plates.index(random.choice(plates))))
                    
     except Exception as err:  
          print('readcar(): ' + str(err))
          logger.debug('readcar(): ' + str(err))
     
     finally:     
          with open('E:\pythontest\\utest\plateno.txt','w') as rewrt:
               for i in plates:
                    rewrt.write(i + '\n')

#车辆入场
def car_in(edit_plate,btn_execute):
     edit_plate.set_text(newplateno.newplate())
     print('车辆：' + edit_plate.text_block() + ' 入场。')
     time.sleep(1)
     btn_execute.click()
     

#车辆出场
def car_out(edit_plate, btn_execute, btn_charge):
     try:
          edit_plate.set_text(readcar())
          if str(edit_plate.text_block()) == str('None'):
               print('无车牌')
               return (0)

          else:
               print('车辆：' + edit_plate.text_block() + ' 出场。')
               time.sleep(2)
               btn_execute.click()
               time.sleep(2)
               btn_charge.click()
          
     except Exception as err:
          print('car_out(): ' + str(err))
          logger.debug('car_out(): ' + str(err))
          


     
     

          


          

     
     
     
     
     
     
     
     
     
