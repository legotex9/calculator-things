#import repl # learn more: https://python.org/pypi/repl
#import sys
#sys.append('C:\Users\Sam downs\Documents\things made in python\python-versions\calcv4-multiple-files\calc.py')
from calc import geometry
from display import menu
s1 = int(0)
s2 = int(0)
s3 = int(0)
q = int(0)
x = float(.25 / 2)
def wip():
	print('work in progress')
	return
while 0 < 1:
    menu.main()
    x = float(0)
    y = float(0)
    z = float(0)
    a = input()
	#area \/ \/
	#square
    if a == 'a1':
        x = float(input(print("side 1 length = ")))
        y = float(input(print("side 2 length = ")))
        z = geometry.area.sqr(x, x, y)
        z = print("area = " + str(z))
        print(z)
	#triangle
    elif a == 'a2':
        x = float(input(print("side length = ")))
        y = float(input(print("height = ")))
        z = geometry.area.tri(x, x, y)
        z = print("area = " + str(z))
        print(z)
	#radius
    elif a == 'a3':
        x = float(input(print("radius = ")))
        z = geometry.area.circle.Radius(1, x)
        z = print("area = " + str(z))
	#diamater
    elif a == 'a4':
        x = float(input(print("diameter = ")))
        z = geometry.area.circle.Diameter(1, x)
        z = print("area = " + str(z))
	#area /\ /\
	#perimiter \/ \/
    elif a == 'p1':
    	x = float(input(print("legth = ")))
    	y = float(input(print("width = ")))
    	z = geometry.perimiter.sqr(1, x, y)
    	z = print("perimiter = " + str(z))
    	print(z)
    elif a == 'p2':
        x = float(input(print("base = ")))
        z = geometry.perimiter.tri(1, x)
        z = print("perimiter = " + str(z))
    elif a == 'p3':

    elif a == 'p4':

	#perimiter /\ /\
	#surface area \/ \/
	#surface area /\ /\
	#volumne \/ \/
	#volume /\ /\
	#other \/ \/
	#other /\ /\


