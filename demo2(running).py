import time
import os
from pywinauto.application import Application
import car_in_out
import random
from random import randint

#连接岗亭收费系统
app = Application().connect(title_re='U.*')

#获取窗口
win_dgg = app.window(title_re='U.*')

a = 0
for i in range(random.randint(1,10)):
     btn_test = win_dgg['测试Button']
     btn_test.click()
     win_cartest = app.window(title='车辆出入测试')
     car_in_out.car_in(win_cartest['车牌号码：Edit'],win_cartest['执行Button'])
     a += 1
print(a)
     

'''
#.netframework窗口，继续
     win_nfw = app.window(title='Microsoft .NET Framework')
#win_nfw.print_control_identifiers()
     time.sleep(1)
     win_nfw['继续(&C)'].click()
     time.sleep(1)
'''     
os.system("pause")




