#暂停1秒输出
import time
from tkinter import Y
for i in range(1,10):
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    time.sleep(1)
