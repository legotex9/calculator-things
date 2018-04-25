import repl # learn more: https://python.org/pypi/repl
from termcolor import colored
import time
import math
#importing main menu
from display import mainMenuNorm, mainMenuNoSleep
#importing area fuctions
from calc import area, perimiter, surfaceArea, volume
s1 = int(0)
s2 = int(0)
s3 = int(0)
q = int(0)
x = float(.25/2)
mem = []

mainMenuNorm()
'''
def note():
	print(colored('NOTE:','red'))
	print(colored('	if you input any character that is not a number, the program will break.','red'))
	print(colored('	i am currently trying to fix it, but it is taking a while.','red'))
	print(colored('	thank you for understanding','red'))
	print(colored(' 		-Kire Brownback','red'))
note()
'''
while q<1:
	pi = math.pi
	x = float(x/2)
	a = float(input())
	x1 = int(1)
	print(mem)
	#lower case alphabet
	alphaLow = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#upper case alphabet
	alphaUp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']
    if a == alphaLow or a == alphaUp:
        print(colored('that is an incorrect input. please try again.','red'))
        break

#exit:
	elif a == 0.03:
		print(colored('shuting','red'))
		time.sleep(1)
		print(colored('down','red'))
		time.sleep(1)
		q = q + 1
 
#show main menu:
	elif a == 0.04:
 		mainMenuNorm()
 		time.sleep(x1)
 		
 
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

#clear screen:
	elif a == 0.07:
		repl.clear()
		
#invalid input:
	else:
		print (colored("that input is not listed or incorect. please try again.","red"))
		time.sleep(x1)

