import time, sys

frase = '.....Aprender tambem é cópiar...'

for i in list(frase):
	print(i, end='')
	sys.stdout.flush()
	time.sleep(0.2)

