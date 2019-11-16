import math
def kwa(a, b, c):
	d = (b * b) -4 * (a * c)
	e = math.sqrt(d)
	f = a * 2
	return( (-b + e)/f, (-b - e)/f)

l = kwa(1 ,5 ,6)
print(l)

