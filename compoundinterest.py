p = input('principal \n')
p = int(p)
r = input('interest rate\n')
r = float(r)
n = input('number of times interest applied per time period\n')
n = int(n)
t = input('number of time periods elapsed\n')
t = int(t)
print('\n')
t1 = t
a = n * t
b = r / n
c = 1 + b
d = c ** a
finalamount = p * d
if finalamount < 1000:
	length = 10
if finalamount > 10000 and finalamount < 100000:
	length = 1000
if finalamount < 100000:
	length = 100
if finalamount > 100000 and finalamount < 1000000:
	length = 10000
if finalamount > 1000000 and finalamount < 1000000000:
	length = 100000
if finalamount > 1000000000:
	length = 50000000
	print('wow')
print(round(finalamount, 2))
while t > 0:
	t -= 1
	a = n * t
	b = r / n
	c = 1 + b
	d = c ** a
	finalamount = p * d
	print(round(finalamount, 2))
	while finalamount > 0:
		print('_', end='')
		finalamount -= length
while t1 > 0:
	print('-', end=' ')
	t1 -= 1