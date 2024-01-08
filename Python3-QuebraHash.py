import hashlib

with open ('dicionario.txt', 'r') as file:
	newfile = file.readlines()
	openfile = newfile
	for x in openfile:
		n1 = x.strip()
		cripter = hashlib.md5(n1.encode()).hexdigest()
		with open ('Hash.txt', 'r') as  encripter:
			newcripter = encripter.readlines()
			opencripter = newcripter
			for Y in opencripter:
				n2 = Y.strip()
				if n2 in cripter:
					print('MD5 Crackeada: {} == {} '.format(n2, n1))
