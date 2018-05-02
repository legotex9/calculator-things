
import math
import time
pi = math.pi
x1 = float(.25)
def colored(a,b):
    return a

class area():
    def Sqr(self, a):
        print(colored('a = l * w','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        a = l*w
        a = str(a)
        time.sleep(x1)
        return a

    def Tri(self, a):
        print(colored('a = (l * w)/2','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        a = (l*w)/2
        a = str(a)
        time.sleep(x1)
        return a

    def Circ(self, a):
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
        print(colored('sa = l*w+l*sqrt((w/2)^2+h^2)+w*sqrt((l/2)^2+h^2)','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        h = float(input('h = '))
        sa = str(l*w+l*math.sqrt((w/2)**2+h**2)+w*math.sqrt((l/2)**2+h**2))
        time.sleep(x1)
        return sa
    def TriangularPyramid(self, sa):
        print(colored('sa = ((b*h)/2)*4','yellow'))
        b = float(input('b = '))
        h = float(input('h = '))
        sa = ((b*h)/2)*4
        time.sleep(x1)
        return sa

    def Sphere(self, sa):
        print('sa = 4 * pi * r ^ 2')
        r = float(input('r = '))
        sa = 4*pi*r**2
        sa = str(sa)
        time.sleep(x1)
        return sa

    def Cylander(self, sa):
        print(colored('(2*(pi*r)*h)+2*(pi*r**2)','yellow'))
        r = float(input('r = '))
        h = float(input('h = '))
        sa = (2*(pi*r)*h)+2*(pi*r**2)
        time.sleep(x1)
        return sa

class volume():
    def Cube(self, v):
        print(colored('v = l * w * h','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        h = float(input('h = '))
        v = str(l*w*h)
        time.sleep(x1)
        return v
    def RectangularPrisim(self, v):
        print(colored('v = l * w * h','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        h = float(input('h = '))
        v = str(l*w*h)
        time.sleep(x1)
        return v
    def TriangularPrisim(self, v):
        print(colored('v = ((b * h1)/2 * h2','yellow'))
        b = float(input('b = '))
        h1 = float(input('h1 = '))
        h2 = float(input('h2 = '))
        v = str(((b*h1)/2)*h2)
        time.sleep(x1)
        return v
    def Cone(self, v):
        print(colored('v = ((pi*r^2)*h)/3','yellow'))
        r = float(input('r = '))
        h = float(input('h = '))
        v = ((pi*r**2)*h)/3
        time.sleep(x1)
        return v
    def RectangularPyramid(self, v):
        print(colored('v = ((l * w) * h)/3','yellow'))
        l = float(input('l = '))
        w = float(input('w = '))
        h = float(input('h = '))
        v = str(((l*w)*h)/3)
        time.sleep(x1)
        return v
    def TriangularPyramid(self, v):
        print(colored('v = (((b * h) /2) * h)/3','yellow'))
        b = float(input('b = '))
        h = float(input('h = '))
        v = str((((b*h)/2)*h)/3)
        time.sleep(x1)
        return v
    def Sphere(self, v):
        print(colored('v = ((pi * r ^ 3) * 4)/3','yellow'))
        r = float(input('r = '))
        v = str(((pi*r**3)*4)/3)
        time.sleep(x1)
        return v
    def Cylander(self, v):
        print(colored('v = (pi * r ^ 2) * h','yellow'))
        r = float(input('r = '))
        h = float(input('h = '))
        v = str((pi*r**2)*h)
        time.sleep(x1)
        return v
