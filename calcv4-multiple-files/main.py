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
def output (type, z):
    a = str(type)
    if type == "area":
        b = print("area = %f" % (z))
        return b
    elif type == "perimiter":
        b = print("perimiter = %f" % (z))
        return b
    elif type == "circumference":
        b = print("circumference = %f" % (z))
        return b
    elif type == "surface area":
        b = print("surface area = %f" % (z))
        return b
    elif type == "volume":
        b = print("volume = %f" % (z))
        return b
menu.main()
print("notes: \n [p1] is currently not working")
while 0 < 1:
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
        print(output('area', z))
	#triangle
    elif a == 'a2':
        x = float(input(print("side length = ")))
        y = float(input(print("height = ")))
        z = geometry.area.tri(x, x, y)
        print(output('area', z))
	#radius
    elif a == 'a3':
        x = float(input(print("radius = ")))
        z = geometry.area.circle.Radius(1, x)
        print(output('area', z))
	#diamater
    elif a == 'a4':
        x = float(input(print("diameter = ")))
        z = geometry.area.circle.Diameter(1, x)
        print(output('area', z))
	#area /\ /\
	#perimiter \/ \/
    #square
    elif a == 'p1':
        wip()
    #	x = float(input(print("legth = ")))
    #	y = float(input(print("width = ")))
    #	z = geometry.perimiter.sqr(1, x, y)
    #    print(output('perimiter',z))
    #triangle
    elif a == 'p2':
        x = float(input(print("base = ")))
        z = geometry.perimiter.tri(1, x)
        print(output('perimiter',z))
    #radius
    elif a == 'p3':
        x = float(input(print("raduius = ")))
        z = geometry.perimiter.circle.Radius(1, x)
        print(output('perimiter',z))
    #diameter
    elif a == 'p4':
        x = float(input(print("diameter = ")))
        z = geometry.perimiter.circle.Diameter(1, x)
        print(output('perimiter',z))
	#perimiter /\ /\
	#surface area \/ \/
    #cube
    elif a == 'sa1':
        x = float(input(print("area for one side= ")))
        z = geometry.surface_area.cube(1,x)
        print(output('surface area',z))
    #prisim-rectangular
    elif a == 'sa2':
        w = float(input(print("length = ")))
        x = float(input(print("width = ")))
        y = float(input(print("height = ")))
        z = geometry.surface_area.prisim.rect(1,w,x,y)
        print(output('surface area',z))
    #prisim-triangular
    elif a == 'sa3':
        v = float(input(print("base perimiter = ")))
        w = float(input(print("height = ")))
        x = float(input(print("triangle height =")))
        y = float(input(print("side length of triangle =")))
        z = geometry.surface_area.prisim.tri(v, w, x, y)
        print(output('surface area',z))
    #pyramid-rectangular
    elif a == 'sa4':
        w = float(input(print("length =")))
        x = float(input(print("height =")))
        y = float(input(print("width =")))
        z = geometry.surface_area.pyramid.rect(w,x,y)
        print(output('surface area',z))
    #pyramid-triangular
    elif a == 'sa5':
        x = float(input(print("base =")))
        y = float(input(print("height =")))
        z = geometry.surface_area.pyramid.tri(x,y)
        print(output('surface area',z))
    #sphere-radius
    elif a == 'sa6':
        x = float(input(print("radius =")))
        z = geometry.surface_area.sphere.radius(x)
        print(output('surface area',z))
    #sphere-diameter
    elif a == 'sa7':
        x = float(input(print("diameter =")))
        z = geometry.surface_area.sphere.diameter(x)
        print(output('surface area',z))
    #cone-radius
    elif a == 'sa8':
        x = float(input(print("radius =")))
        y = float(input(print("height =")))
        z = geometry.surface_area.cone.radius(x,y)
        print(output('surface area',z))
    #cone-diameter
    elif a == 'sa9':
        x = float(input(print("diameter =")))
        y = float(input(print("height =")))
        z = geometry.surface_area.cone.diameter(x,y)
        print(output('surface area',z))
    #cylinder-radius
    elif a == 'sa10':
        x = float(input(print("radius =")))
        y = float(input(print("height =")))
        z = geometry.surface_area.cylinder.radius(x,y)
        print(output('surface area',z))
    #cylinder-diameter
    elif a == 'sa11':
        x = float(input(print("diameter =")))
        y = float(input(print("height =")))
        z = geometry.surface_area.cylinder.diameter(x,y)
        print(output('surface area',z))
	#surface area /\ /\
	#volume \/ \/
    #cube
    elif a == 'v1':
        x = float(input(print("side length =")))
        z = geometry.volume.cube(1)
        print(output('volume',z))
    #rectangular prisim
    elif a == 'v2':
        w = float(input(print("length =")))
        x = float(input(print("height =")))
        y = float(input(print("width =")))
        z = geometry.volume.prisim.rect(w,x,y)
        print(output('volume',z))
    #triangular prisim
    elif a == 'v3':
        w = float(input(print("base =")))
        x = float(input(print("tri angle height =")))
        y = float(input(print("length =")))
        z = geometry.volume.prisim.tri(w,x,y)
        print(output('volume',z))
    #rectangular pyramid
    elif a == 'v4':
        w = float(input(print("base length =")))
        x = float(input(print("base width =")))
        y = float(input(print("height =")))
        z = geometry.volume.pyramid.rect(w,x,y)
        print(output('volume',z))
    #triangular pyramid
    elif a == 'v5':
        w = float(input(print("base length =")))
        x = float(input(print("base width =")))
        y = float(input(print("height =")))
        z = geometry.volume.pyramid.tri(w,x,y)
        print(output('volume',z))
    #sphere with radius
    elif a == 'v6':
        x = float(input(print("radius =")))
        z = geometry.volume.sphere.radius(x)
        print(output('volume',z))
    #sphere w/ diameter
    elif a == 'v7':
        x = float(input(print("diameter =")))
        z = geometry.volume.sphere.diameter(x)
        print(output('volume',z))
    #cone w/ radius
    elif a == 'v8':
        x = float(input(print("radius =")))
        y = float(input(print("height =")))
        z = geometry.volume.cone.radius(x)
        print(output('volume',z))
    #con w/ cylinder
    elif a == 'v9':
        x = float(input(print("diameter =")))
        y = float(input(print("height =")))
        z = geometry.volume.cone.diameter(x)
        print(output('volume',z))
    #cylinder w/ radius
    elif a == 'v10':
        x = float(input(print("radius =")))
        y = float(input(print("height =")))
        z = geometry.volume.cylinder.radius(x)
        print(output('volume',z))
    #cylinder w/ diameter
    elif a == 'v11':
        x = float(input(print("diameter =")))
        y = float(input(print("height =")))
        z = geometry.volume.cylinder.diameter(x)
        print(output('volume',z))
	#volume /\ /\
	#other \/ \/
    elif a == 'main menu':
        menu.main()
	#other /\ /\