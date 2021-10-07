import time
import os
import shutil

pathin = input("Enter the file name")
pathout = input("Enter your destination")
pathin = pathin + '/'
pathout = pathout + '/'
ti = time.time()
check = os.path.exists(pathin)
if check == True:
    returning = os.walk(pathin)
    joining = os.path.join(pathin,pathout)
ctime = os.stat(pathin).st_ctime
if ctime > ti:
    removeing = os.remove(pathin)
    print("Path doesnot exist")
