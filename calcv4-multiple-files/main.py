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
    v = float(0)
    w = float(0)
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
    #square
    elif a == 'p1':
    	x = float(input(print("legth = ")))
    	y = float(input(print("width = ")))
    	z = geometry.perimiter.sqr(1, x, y)
    	z = print("perimiter = " + str(z))
    	print(z)
    #triangle
    elif a == 'p2':
        x = float(input(print("base = ")))
        z = geometry.perimiter.tri(1, x)
        z = print("perimiter = " + str(z))
    #radius
    elif a == 'p3':
        x = float(input(print("raduius = ")))
        z = geometry.perimiter.circle.Radius(1, x)
        z = print("circumference = " + str(z))
    #diameter
    elif a == 'p4':
        x = float(input(print("diameter = ")))
        z = geometry.perimiter.circle.Diameter(1, x)
        z = print("circumference = " + str(z))
	#perimiter /\ /\
	#surface area \/ \/
    #cube
    elif a == 'sa1':
        x = float(input(print("area for one side= ")))
        z = geometry.surface_area.cube(1,x)
        z = print("surface area = " + str(Z))
    #prisim-rectangular
    elif a == 'sa2':
        w = float(input(print("length = ")))
        x = float(input(print("width = ")))
        y = float(input(print("height = ")))
        z = geometry.surface_area.prisim.rect(1,w,x,y)
        z = print("surface area = " + str(z))
    #prisim-triangular
    elif a == 'sa3':
        v = float(input(print("base perimiter = ")))
        w = float(input(print("height = ")))
        x = float(input(print("triangle height =")))
        y = float(input(print("side length of triangle =")))
        z = geometry.surface_area.prisim.tri(v, w, x, y)
        z = print("surface area ="  + str(z))
    #pyramid-rectangular
    elif a == 'sa4':
        w = float(input(print("length =")))
        x = float(input(print("height =")))
        y = float(input(print("width =")))
        z = geometry.surface_area.pyramid.rect(w,x,y)
        z = print("surface area = " + str(z))
    #pyramid-triangular
    elif a == 'sa5':
    #sphere-radius
    elif a == 'sa6':
    #sphere-diameter
    elif a == 'sa7':
    #cone-radius
    elif a == 'sa8':
    #cone-diameter
    elif a == 'sa9':
    #cylinder-radius
    elif a == 'sa10':
    #cylinder-diameter
    elif a == 'sa11':
	#surface area /\ /\
	#volumne \/ \/
	#volume /\ /\
	#other \/ \/
	#other /\ /\


