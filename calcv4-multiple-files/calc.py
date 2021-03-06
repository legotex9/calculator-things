import math
import time
pi = math.pi
x1 = float(.25)
def sqrt(a):
    b = math.sqrt(a)
    return b
def sqrd(a):
    b = a**2
    return b
class geometry():
    class area():
        def sqr (self, length, width):
            area = length*width
            return area
        def tri (self, base, height):
            area = (base*height)/2
            return area
        class circle():
            def Radius (self, radius):
                area = pi*radius**2
                return area
            def Diameter (self, diameter):
                area = pi*(diameter/2)**2
                return area
    class perimiter():
        def sqr( self, length, width):
            perm = (length*2)+(width*2)
            return perm
        def tri (self, base):
            perm = base*3
            return perm
        class circle():
            def Radius (self, radius):
                perm = 2*pi*radius
                return perm
            def Diameter (self, diameter):
                perm = pi*diameter
                return perm
    class surface_area():
        def cube (self, area_of_one_side):
            SA = area_of_one_side*6
            return SA
        class prisim():
            def rect (self, length, width, height):
                SA = 2*(width*length+height*length+height*width)
                return SA
            def tri (self, perimiter_of_base, height, tri_height, tri_base):
                SA = perimiter_of_base*height+geometry.area.tri(tri_base, tri_height)
                return SA
        class pyramid():
            def rect (self, length, width, height):
                l = length
                h = height
                w = width
                SA = l*w+l*sqrt(sqrd(w/2)+sqrd(h))+w*sqrt(sqrd(l/2)+sqrd(height))
                return SA
            def tri (self, base, height):
                SA = ((base*height)/2)*4
                return SA
        class sphere():
            def radius (self, radius):
                SA = 4*pi*radius**2
                return SA
            def diameter(self, diameter):
                return geometry.surface_area.sphere.radius(diameter/2)
        class cone():
            def radius(self, radius, height):
                SA = pi*radius*(radius+sqrt(sqrd(height)+sqrd(radius)))
                return SA
            def diameter(self, diameter, height):
                return geometry.surface_area.cone.radius()
        class cylinder():
            def radius(self, radius, height):
                SA = geometry.perimiter.circle(radius)*height+geometry.area.circle(radius)*2
                return SA
            def diameter(self, diameter, height):
                radius = diameter/2
                SA = geometry.perimiter.circle(radius)*height+geometry.area.circle(radius)*2
                return SA
    class volume():
        def cube(self, side_length):
            v = side_length**3
            return v
        class prisim():
            def rect(self, length, width, height):
                v = length*width*height
                return v
            def tri(self, base, height1, height2):
                v = ((base*height1)/2)*height2
                return v
        class pyramid():
            def rect(self, base_length, base_width, height):
                v = ((base_length*base_width)*height)/3
                return v
            def tri(self, base_length, base_height, height):
                v = (((base_length*base_height)/2)*height)/3
                return v
        class sphere():
            def radius(self, radius):
                v = ((pi*r**3)*4)/3
                return v
            def diameter(self, diameter):
                v = geometry.volume.sphere.radius(diameter/2)
                return v
        class cone():
            def radius(self, radius, height):
                v = ((pi*sqrd(r))*height)/3
                return v
            def diameter(self, diameter, height):
                v = geometry.volume.cone.radius(diameter/2, height)
                return v
        class cylinder():
            def radius(self, radius, height):
                v = (pi*sqrd(r))*height
                return v
            def diameter(self, diameter, height):
                v = geometry.volume.cylinder.radius(diameter/2,height)
                return v

class other():
    def pythag(a,b):
        a2 = a**2
        b2 = b**2
        a2b2 = a2+b2
        final = sqrt(a2b2)
        return final