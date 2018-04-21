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
        print(colored('a = pi * r^2','yellow'))
        r = float(input('r = '))
        a = pi*r**2
        a = str(a)
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
        print(colored('p = 2 * pi * r'))
        r = float(input('r = '))
        p = 2*pi*r
        p = str(p)
        time.sleep(x1)
        return p
	
class surfacearea():
    def Cube(self, sa):
        print(colored('sa = ( l * w )* 6','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        sa = (l*w)*6
        sa = str(sa)
        time.sleep(x1)
        return sa
    def RectangularPrisim(self, sa):
        print(colored('sa = (p * h) + (2 * (l * w))','yellow'))
        p = float(input('p = '))
        h = float(input('h = '))
        l = float(input('l = '))
        w = float(input('w = '))
        sa = (p*h)+(2*(l*w))
        sa = str(sa)
        time.sleep(x1)
        return sa
    def TriangularPrisim(self, sa):
        print(colored('sa = (p * h) + (2 * ((l * w)/2))','yellow'))
        p = float(input('p = '))
        h = float(input('h = '))
        l = float(input('l = '))
        w = float(input('w = '))
        sa = (p*h)+(2*((l*w)/2))
        sa = str(sa)
        time.sleep(x1)
        return sa
    def Cone(self, sa):
        print(colored('sa = pi * r * (r + sqrt(h^2 + r^2))','yellow'))
        r = float(input('r = '))
        h = float(input('h = '))
        sa = pi*r*(r+math.sqrt(h**2+r**2))
        sa = str(sa)
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
        print('sa = 4 * pi * r ^ 2')
        r = float(inptu('r = '))
        sa = 4*pi*r**2
        sa = str(sa)
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

class equations():
    def pythagA(self, A):
        print('wip')
        time.sleep(x1)
        return A
    def pythagB(self, B):
        print('wip')
        time.sleep(x1)
        return B
    def pythagC(self, C):
        print('wip')
        time.sleep(x1)
        return C
    
class conversionMath():
   def CeltoFar(self, f):
       c = float(input('celcius = '))
       f = c*1.8+32
       f = str(f)
       time.sleep(x1)
       return f
   def FartoCel(self, f):
       f = float(input('fahrenheit = '))
       c = (f-32)/1.8
       c = str(c)
       time.sleep(x1)
       return a
