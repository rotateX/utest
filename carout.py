import time
import os
from pywinauto.application import Application
import car_in_out
import random


#连接到岗亭收费系统
app = Application().connect(title_re='U.*')

#获取收费系统主窗口
win_dgg = app.window(title_re='U.*）')



for i in range(random.randint(1,15)):
     btn_test = win_dgg['测试button4']
     btn_test.click()
     
#读取车牌，执行     
     win_cartest = app.window(title='车辆出入测试')
     win_car = app['WindowsForms10.Window.8.app.0.2bf8098_r15_ad1']
     a = car_in_out.car_out(win_cartest['车牌号码：Edit'],
                            win_cartest['执行Button4'],
                            win_car['收费放行Button'])
     if a == 0:
          time.sleep(1)
          win_cartest['取消'].click()
          break
     


'''
#车辆出场
     win_car = app['WindowsForms10.Window.8.app.0.2bf8098_r15_ad1']
     time.sleep(1)

     win_car['收费放行Button'].click()
     time.sleep(random.randint(1,5))
'''

