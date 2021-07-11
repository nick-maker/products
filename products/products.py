products = []
while True:
	name = input('What did you buy:')
	if name == 'q':
		break
	dollar = input('How much was it:')
	products.append([name, dollar])
print(products)

for p in products:
	print(p[0], 'is', p[1], 'dollars')