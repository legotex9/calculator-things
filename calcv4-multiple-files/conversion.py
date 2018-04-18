import time
from termcolor import colored
#conversion menu:
class conversionStuff():
	#menu
	def conversionMenu():
		print (colored('|[][][][][][][][][][][][][][][]|','blue'))
		print (colored('| CELCIUS TO FAHRENHEIT | 6.01 |','blue'))
		print (colored('| FAHRENHEIT TO CELCIUS | 6.02 |','blue'))
		print (colored('|::::::::::::::::::::::::::::::|','blue'))
		print (colored('|    FEET TO INCHES     | 6.03 |','blue'))
		print (colored('|    FEET TO MILES      | 6.04 |','blue'))
		print (colored('|    FEET TO YARDS      | 6.05 |','blue'))
		print (colored('|    FEET TO METERS     | 6.06 |','blue'))
		print (colored('|  FEET TO KILOMETERS   | 6.07 |','blue'))
		print (colored('| FEET TO CENTIMETERS   | 6.08 |','blue'))
		print (colored('|  FEET TO MILIMETERS   | 6.09 |','blue'))
		print (colored('|::::::::::::::::::::::::::::::|','blue'))
		print (colored('|     INCHES TO FEET    | 6.10 |','blue'))
		print (colored('|    INCHES TO MILES    | 6.11 |','blue'))
		print (colored('|    INCHES TO YARDS    | 6.12 |','blue'))
		print (colored('|   INCHES TO METERS    | 6.13 |','blue'))
		print (colored('|  INCHES TO KILOMETERS | 6.14 |','blue'))
		print (colored('| INCHES TO CENTIMETERS | 6.15 |','blue'))
		print (colored('|  INCHES TO MILIMETERS | 6.16 |','blue'))
		print (colored('|[][][][][][][][][][][][][][][]|','blue'))
	
	def CelToFar(self, f):
		c = float(input('celcius = '))
		f = c*1.8+32
		f = str(f)
		time.sleep(1)
		return (f)

	def FarToCel(self, c):
		f = float(input*'fahrenheit = ')
		c = (f-32)/1.8
		c = str(c)
		time.sleep(1)
		return(c)
