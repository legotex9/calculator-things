from termcolor import colored
import math
import time
pi = math.pi
x1 = float(.25)

class area():
    def areaSqr(self, a):
        print(colored('a = l * w','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        a = l*w
        a = str(a)
        time.sleep(x1)
        return a
    
    def areaTri(self, a):
        print(colored('a = (l * w)/2','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        a = (l*w)/2
        a = str(a)
        time.sleep(x1)
        return a
    
    def areaCirc(self, a):
        print('wip')
        time.sleep(x1)
        return a

class perimiter():
    def Sqr(self, p):
        print(colored('p = l * 4','yellow'))
        l = float(input('l = '))
        p = l*4
        p = str(p)
        time.sleep(x1)
        return p
    def Tri(self, p):
        print(colored('p = l * 3','yellow'))
        l = float(input('l = '))
        p = l*3
        p = str(p)
        time.sleep(x1)
        return p
    def Circ(self, p):
        print('wip')
        return p
	
class surfacearea():
    def Cube(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def RectangularPrisim(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def TriangularPrisim(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def Cone(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def RectangularPyramid(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def TriangularPyramid(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def Sphere(self, sa):
        print('wip')
        time.sleep(x1)
        return sa
    def Cylander(self, sa):
        print('wip')
        time.sleep(x1)

class volume():
    def Cube(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def RectangularPrisim(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def TriangularPrisim(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def Cone(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def RectangularPyramid(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def TriangularPyramid(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def Sphere(self, v):
        print('wip')
        time.sleep(x1)
        return v
    def Cylander(self, v):
        print('wip')
        time.sleep(x1)
        return v
