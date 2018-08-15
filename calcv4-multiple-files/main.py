#import repl # learn more: https://python.org/pypi/repl
#import sys
#sys.append('C:\Users\Sam downs\Documents\things made in python\python-versions\calcv4-multiple-files\calc.py')
import time
import math
from calc import geometry
from display import menu


s1 = int(0)
s2 = int(0)
s3 = int(0)
q = int(0)
x = float(.25/2)


while 0<1:
    x = float(0)
    y = float(0)
    z = float(0)
    menu.main()
    a = input()
    if a == "g1":
        x = float(input(print("side 1 length = ")))
        y = float(input(print("side 2 length = ")))
        z = geometry.area.sqr(x,x,y)
        z = print("area = " + str(z))
        print (z)
    elif a == 'g2':
        x = float(input(print("side length = ")))
        y = float(input(print("height = ")))
        z = geometry.area.tri(x,x,y)
        z = print("area = " + str(z))
        print(z)
        break


