import repl # learn more: https://python.org/pypi/repl
from termcolor import colored
import time
import math
#importing main menu
from display import mainMenuNorm, mainMenuNoSleep
#importing area fuctions
from calc import area, perimiter, surfaceArea, volume
#importing conversion stuff
from conversion import conversionStuff
s1 = int(0)
s2 = int(0)
s3 = int(0)
q = 0
x = float(.25/2)
mem = []

mainMenuNorm()
def note():
	print(colored('NOTE:','red'))
	print(colored('	if you input any character that is not a number, the program will break.','red'))
	print(colored('	i am currently trying to fix it, but it is taking a while.','red'))
	print(colored('	thank you for understanding','red'))
	print(colored(' 		-Kire Brownback','red'))
note()
while q<1:
	pi = math.pi
	x = float(x/2)
	a = float(input())
	x1 = int(1)
	print(mem)
	alphaLow = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alphaUp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']
    if a == alphaLow or a == alphaUp:
        print(colored('that is an incorrect input. please try again.','red'))
        break
# --------------------------------------------
#area:
	#area of square
	if a == 1.01:
		print(colored('a = l * w', 'yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		a = float(l * w)
		a = str(a)
		print (colored('a = ' + a, 'green'))
		time.sleep(x1)
		mem.append(a)
	
	#area of triangle
	elif a == 1.02:
		print(colored('a = (h * b)/2','yellow'))
		h = float(input('h = '))
		b = float(input('b = '))
		a = (h*b)/2
		a = str(a)
		print (colored('a = ' + a, 'green'))
		time.sleep(x1)
		mem.append(a)
	
	#area of circle
	elif a == 1.03:
		if s1 == 0:
			print(colored('a = pi * r ^ 2','yellow'))
			r = float(input('r = '))
			a = pi * r **2
			a = str(a)
			print (colored('a = ' + a,'green'))
		else:
			print(colored('a = pi * d ^ 2','yellow'))
			d = float(input('d = '))
			a = pi * (d/2) **2
			a = str(a)
			print (colored('a = ' + a,'green'))
			mem.append(a)
	
#	------------------------------------------------
	
#perimiter:
	#perimiter of squrae
	elif a == 2.01:
		print(colored('p = (2 * l) + (2 * w)', 'yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		p = float((2*l) + (2*w))
		p = str(p)
		print(colored('p = ' + p, 'green'))
		time.sleep(x1)
		mem.append(p)
	
	#perimiter of triangle
	elif a == 2.02:
		print(colored(' p = 3*s','yellow'))
		s = float(input('s = '))
		p = s*3
		p = str(p)
		print(colored('p = ' + p, 'green'))
		time.sleep(x1)
		mem.append(p)
	
	#perimiter of circle
	elif a == 2.03:
		if s1 == 0:
			print(colored('p = 2 * pi* r','yellow'))
			r = float(input('r = '))
			p = 2 * pi * r
			p = str(p)
			print(colored('p = ' + p,'green'))
			time.sleep(x1)
			mem.append(p)
		else:
			print(colored('p = 2 * pi* d','yellow'))
			d = float(input('d = '))
			p = 2 * pi * (d/2)
			p = str(p)
			print(colored('p = ' + p,'green'))
			time.sleep(x1)
			mem.append(p)
			
#	------------------------------------------------
	
#surface area:
	#surface area of cube
	elif a == 3.01:
		print(colored('sa = 6 * b ^ 2','yellow'))
		b = float(input('b = '))
		sa = float(6*b**2)
		sa = str(sa)
		print(colored('sa = ' + sa, 'green'))
		time.sleep(x1)
		mem.append(sa)
	
	#surface area of rectangular prism
	elif a == 3.02:
		print(colored('sa = 2 * (w * l + h * l + h * w)  ','yellow'))
		w = float(input('w = '))
		l = float(input('l = '))
		h = float(input('h = '))
		sa = 2*(w*l+h*l+h*w)
		sa = str(a)
		print (colored('sa = ' + sa, 'green'))
		time.sleep(x1)
		mem.append(sa)
		
	#surface area of triangular prisim
	elif a == 3.03:
		print(colored('sa = ((b * h1)/2) * h2','yellow'))
		b = float(input('b = '))
		h1 = float(input('h1 = '))
		h2 = float(input('h2 = '))
		sa = ((b*h1)/2)*h2
		sa = str(sa)
		print(colored('sa = ' + sa,'green'))
		time.sleep(x1)
		mem.append(sa)
		
	#surface area of cone
	elif a == 3.04:
		if s1 == 0:
			print(colored('sa = pi * r *(r + sqrt(h ^ 2 + r^2))','yellow' ))
			r = float(input('r = '))
			h = float(input('h = '))
			sa = pi*r*(r + math.sqrt(h**2+r**2))
			sa = str(sa)
			print(colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
		else:
			print(colored('sa = pi * d *(d + sqrt(h ^ 2 + d^2))','yellow' ))
			d = float(input('d = '))
			d = d/2
			h = float(input('h = '))
			sa = pi*r*(d + math.sqrt(h**2+d**2))
			sa = str(sa)
			print(colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
	
	#surface area of rectangular pyramid
	elif a == 3.05:
		print(colored('l * w + l * sqrt( (w/2) ^ 2 + h ^ 2) + sqrt( (l/2) ^ 2 + h ^ 2)','yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		h = float(input('h = '))
		sa = l*w+l*math.sqrt((w/2)**2+h**2)+w*math.sqrt((l/2)**2+h**2)
		sa = str(sa)
		print(colored('sa = ' + sa,'green'))
		time.sleep(x1)
		mem.append(sa)
	
	#surface area of triangular pyramid
	elif a == 3.06:
		print(colored('sa = ((b * h)/2) * 4','yellow'))
		b = float(input('b = '))
		h = float(input('h = '))
		sa = ((b*h)/2)*4
		sa = str(sa)
		print(colored('sa = ' + sa,'green'))
		time.sleep(x1)
		mem.append(sa)
	
	#surface area of sphere
	elif a == 3.07:
		if s1 == 0:
			print(colored('sa = 4 * (pi * r ^2)','yellow'))
			r = float(input('r = '))
			sa = 4*(pi*r**2)
			sa = str(sa)
			print(colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
		else:
			print(colored('sa = 4 * (pi * d ^2)','yellow'))
			d = float(input('d = '))
			d = d/2
			sa = 4*(pi*r**2)
			sa = str(sa)
			print(colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
			
	#surfeace area of cylinder
	elif a == 3.08:
		if s1 == 0:
			print(colored('sa = (2 * (pi * r) * h) + 2 * (pi * r ^ 2)','yellow'))
			r = float(input('r ='))
			h = float(input('h ='))
			sa = (2*(pi*r)*h)+2*(pi*r**2)
			sa = str(sa)
			print (colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
		else:
			print(colored('sa = (2 * (pi * r) * h) + 2 * (pi * r ^ 2)','yellow'))
			d = float(input('d ='))
			d = d/2
			h = float(input('h ='))
			sa = (2*(pi*r)*h)+2*(pi*r**2)
			sa = str(sa)
			print (colored('sa = ' + sa,'green'))
			time.sleep(x1)
			mem.append(sa)
		
#	------------------------------------------------
	
#volume:
	#volume of cube
	elif a == 4.01:
		print(colored('v = l * w * h','yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		h = float(input('h = '))
		v = l*w*h
		v = str(v)
		print(colored('v = ' + v, 'green'))
		time.sleep(x1)
		mem.append(v)
		
	#volume of rectangular prisim
	elif a == 4.02:
		print(colored('v = w * l * h','yellow'))
		w = float(input('w = '))
		l = float(input('l = '))
		h = float(input('h = '))
		v = w*l*h
		v = str(v)
		print(colored('v = ' + v, 'green'))
		time.sleep(x1)
		mem.append(v)
		
	#volume of triangular prisim
	elif a == 4.03:
		print(colored('sa = ((b * h1)/2) * h2','yellow'))
		b = float(input('b = '))
		h1 = float(input('h1 = '))
		h2 = float(input('h2 = '))
		sa = ((b*h1)/2)*h2
		sa = str(sa)
		print(colored('sa = ' + sa,'green'))
		time.sleep(x1)
		mem.append(v)
	
	#volume of cone
	elif a == 4.04:
		if s1 == 0:
			print(colored('v = ((pi * r ^ 2) * h) /3','yellow'))
			r = float(input('r = '))
			h = float(input('h = '))
			v = ((pi * r**2)*h)/3
			v = str(v)
			print(colored('v = ' + v,'green'))
			mem.append(v)
		else:
			print(colored('v = ((pi * r ^ 2) * h) /3','yellow'))
			d = float(input('d = '))
			d = d/2
			h = float(input('h = '))
			v = ((pi * r**2)*h)/3
			v = str(v)
			print(colored('v = ' + v,'green'))
			mem.append(v)
		
	#volume of rectangular pyramid
	elif a == 4.05:
		print(colored('v = ((l * w) * h) /3','yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		h = float(input('h = '))
		v = ((l*w)*h)/3 
		v = str(v)
		print(colored('v = ' + v,'green'))
		time.sleep(x1)
		mem.append(v)
	
	#volume of triangular pyramid
	elif a == 4.06:
		print(colored('v = (((b * h)/2) * h)/3','yellow'))
		b = float(input('b = '))
		h = float(input('h = '))
		v = (((b*h)/2)*h)/3
		v = str(a)
		print(colored('v = ' + a,'green'))
		time.sleep(x1)
		mem.append(v)
	
	#volume of sphere
	elif a == 4.07:
		if s1 == 0:
			print(colored('v = ((pi * r ^ 3) * 4) /3'))
			r = float(input('r = '))
			v = ((pi*r**3)*4)/3
			v = str(v)
			print(colored('v = ' + v,'green'))
			mem.append(v)
		else:
			print(colored('v = ((pi * r ^ 3) * 4) /3'))
			d = float(input('d = '))
			d = d/2
			v = ((pi*r**3)*4)/3
			v = str(v)
			print(colored('v = ' + v,'green'))
			mem.append(v)
		
	#volume of cylinder
	elif a == 4.08:
		if s1 == 0:
			print(colored(' (pi * r ^2) * h','yellow'))
			r = float(input('r = '))
			h = float(input('h = '))
			v = (pi*r**2)*h
			v = str(v)
			print(colored('v = ' + v,'green'))
			time.sleep(x1)
			mem.append(v)
		else:
			print(colored(' (pi * r ^2) * h','yellow'))
			d = float(input('d = '))
			d = d/2
			h = float(input('h = '))
			v = (pi*d**2)*h
			v = str(v)
			print(colored('v = ' + v,'green'))
			time.sleep(x1)
			mem.append(v)
		
#	------------------------------------------------
	
#varible translation:
	elif a == 0.01:
		print('wip')
		time.sleep(x1)
		
#	------------------------------------------------
	
#equations used:
	elif a == 0.02:
		x1 = x1/8
	#area equations:
		print(colored('area equations:','yellow'))
		time.sleep(x1)
		print(colored('	square','yellow'))
		time.sleep(x1)
		print(colored('  a = l * w ','yellow'))
		time.sleep(x1)
		print(colored('	triangle','yellow'))
		time.sleep(x1)
		print(colored('  a = (h*b)/2 ','yellow'))
		time.sleep(x1)
		print(colored('	circle','yellow'))
		time.sleep(x1)
		print(colored('  a = pi * r ^ 2 \n \n','yellow'))
		time.sleep(x1)
		
		
	#perimiter equations:
		print(colored('preimiter equations:','yellow'))
		time.sleep(x1)
		print(colored('	square','yellow'))
		time.sleep(x1)
		print(colored('  p (2 * l) + (2 * w)= ','yellow'))
		time.sleep(x1)
		print(colored('	triangle','yellow'))
		time.sleep(x1)
		print(colored('  p = 3 * s ','yellow'))
		time.sleep(x1)
		print(colored('	circle','yellow'))
		time.sleep(x1)
		print(colored('  p = 2 * pi * r \n \n','yellow'))
		time.sleep(x1)
		
		
 #surface area equations:
		print(colored('preimiter equations:','yellow'))
		time.sleep(x1)
		
		print(colored(' prisims','yellow'))
		time.sleep(x1)
		
		print(colored('  rectangular','yellow'))
		time.sleep(x1)
		print(colored('  sa = 2 * (w * l + h * l + h * w) ','yellow'))
		time.sleep(x1)
		
		print(colored('  triangular','yellow'))
		time.sleep(x1)
		print(colored('  sa = ((b * h1)/2)* h2 ','yellow'))
		time.sleep(x1)
		
		print(colored(' pyramids','yellow'))
		time.sleep(x1)
		
		print(colored('  rectangular','yellow'))
		time.sleep(x1)
		print(colored('  sa = l * w + l * sqrt( (w/2) ^ 2 + h ^ 2) + sqrt( (l/2) ^ 2 + h ^ 2) ','yellow'))
		time.sleep(x1)
	
		print(colored('  triangular','yellow'))
		time.sleep(x1)
		print(colored('  sa = ((b * h)/2) * 4 ','yellow'))
		time.sleep(x1)
		
		print(colored(' sphere','yellow'))
		time.sleep(x1)
		print(colored('  sa = 4 * (pi * r ^2) ','yellow'))
		time.sleep(x1)
		
		print(colored(' cylander','yellow'))
		time.sleep(x1)
		print(colored('  sa = (2 * (pi * r) * h) + 2 * (pi * r ^ 2) ','yellow'))
		time.sleep(x1)
		
		print(colored(' cone','yellow'))
		time.sleep(x1)
		print(colored('  sa = pi * r *(r + sqrt(h ^ 2 + r^2)) ','yellow'))
		time.sleep(x1)
		
		print(colored(' cube','yellow'))
		time.sleep(x1)
		print(colored('  sa = 6 * b ^ 2 \n \n','yellow'))
		time.sleep(x1)
	
	
	#volume equations:
		print(colored('preimiter equations:','yellow'))
				
		print(colored(' prisims','yellow'))
		time.sleep(x1)
		
		print(colored('  rectangular','yellow'))
		time.sleep(x1)
		print(colored('  v = w * l * h ','yellow'))
		time.sleep(x1)
		
		print(colored('  triangular','yellow'))
		time.sleep(x1)
		print(colored('  v = ((b * h1)/2)* h2 ','yellow'))
		time.sleep(x1)
		
		print(colored(' pyramids','yellow'))
		time.sleep(x1)
		
		print(colored('  rectangular','yellow'))
		time.sleep(x1)
		print(colored('  v = ((l * w) * h)/3 ','yellow'))
		time.sleep(x1)
	
		print(colored('  triangular','yellow'))
		time.sleep(x1)
		print(colored('  v = (((b * h)/2 * h)/3 ','yellow'))
		time.sleep(x1)
		
		print(colored(' sphere','yellow'))
		time.sleep(x1)
		print(colored('  v = ((pi * r ^ 3) * 4)/3 ','yellow'))
		time.sleep(x1)
		
		print(colored(' cylander','yellow'))
		time.sleep(x1)
		print(colored('  v = (2 * (pi * r) * h) + 2 * (pi * r ^ 2) ','yellow'))
		time.sleep(x1)
		
		print(colored(' cone','yellow'))
		time.sleep(x1)
		print(colored('  v = ((pi * r ^ 2) * h)/3 ','yellow'))
		time.sleep(x1)
		
		print(colored(' cube','yellow'))
		time.sleep(x1)
		print(colored('  v = w*l*h \n \n','yellow'))
		time.sleep(x1)
		
		
		x1 = x1*2
	
#	------------------------------------------------
	
#exit:
	elif a == 0.03:
		print(colored('shuting','red'))
		time.sleep(1)
		print(colored('down','red'))
		time.sleep(1)
		q = q + 1
	
#	------------------------------------------------
 
#show main menu:
	elif a == 0.04:
 		mainMenuNorm()
 		time.sleep(x1)
 		
#	------------------------------------------------
 
#settings:
	elif a == 0.05:
		print (colored('|radius or diameter | R | s1 |','cyan'))
		S = input('setting id = ')
		if S == 's1':
			if s1 == 0: 
				s1 = s1 + 1
				print (colored('setting updated','green'))
			else:
				s1 = s1 -1
				print (colored('setting updated','green'))
		
 			
#	------------------------------------------------
 
#pythag menu:
	elif a == 5.01:
		print(colored('||||||||||||||||||||||||','cyan'))
		print(colored('| A^2 + B^2 = [C^2] |p1|','cyan'))
		print(colored('||||||||||||||||||||||||','cyan'))
		print(colored('| A^2 + [B^2] = C^2 |p2|','cyan'))
		print(colored('||||||||||||||||||||||||','cyan'))
		print(colored('| [A^2] + B^2 = C^2 |p3|','cyan'))
		print(colored('||||||||||||||||||||||||','cyan'))
		p = input()
		#pythag equations and solver
		#finding c
		if p == 'p1' or p == 'P1':
			a = float(input('a = '))
			b = float(input('b = '))
			a1 = a**2
			b1 = b**2
			c1 = math.sqrt(a1+b1)
			c1 = str(c1)
			b = str(b)
			a = str(a)
			print (colored(a + ' + ' + b + ' = ' + c1,'green'))
			time.sleep(x1)
			mem.append(c1)
			
		#finding b
		elif p == 'p2' or p == 'P2':
			a = float(input('a = '))
			c = float(input('c = '))
			a1 = a**2
			c1 = c**2
			b1 = math.sqrt(c - a)
			b1 = str(b1)
			c = str(c)
			a = str(a)
			print (colored(a + ' + ' + b1 + ' = ' + c,'green'))
			time.sleep(x1)
			mem.append(b1)
			
		#finding a
		elif p == 'p3' or p == 'P3':
			b = float(input('b = '))
			c = float(input('c = '))
			a1 = b**2
			c1 = c**2
			a1 = math.sqrt(c - b)
			a1 = str(b1)
			b = str(b)
			c = str(c)
			print (colored(a1 + ' + ' + b + ' = ' + c,'green'))
			time.sleep(x1)
			mem.append(a1)
 
# ------------------------------------------------ 

#simple intrest:
	elif a == 5.02:
		print(colored('I = Prt','yellow'))
		p = float(input('P = '))
		r = float(input('r = '))
		t = float(input('t = '))
		i = p*r*t
		i = str(i)
		print (colored('I = ' + i,'green'))
		time.sleep(x1)
		mem.append(i)

# ------------------------------------------------

#compund intrest:
	elif a == 5.03:
		print (colored('A = P(1 + r)^t','yellow'))
		p = float(input('P = '))
		r = float(input('r = '))
		t = float(input('t = '))
		a = a*(1+r)**t
		a = str(a)
		print (colored('A = ' + a,'green'))
		time.sleep(x1)
		mem.append(a)
		
# ------------------------------------------------


# ------------------------------------------------

#clear screen:
	elif a == 0.07:
		repl.clear()
		
# ------------------------------------------------
		
#invalid input:
	else:
		print (colored("that input is not listed or incorect. please try again.","red"))
		time.sleep(x1)

