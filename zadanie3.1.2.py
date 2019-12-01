def wyiksuj(zdanie):
	ns =' '
	for slowo in zdanie:
		if slowo in 'QWERTYUIOPASDFGHJKLZXCVBNM':
			ns = ns + 'X'
		elif slowo in 'qwertyuiopasdfghjklzxcvbnm':
			ns = ns + 'x'
		else:
			ns = ns + slowo
	print (ns)
q= wyiksuj('Python 3.6.1 (default, Dec 2015, 13:05:11)')

print('\n')
		
	
