products = []
while True:
	name = input('What did you buy:')
	if name == 'q':
		break
	dollar = input('How much was it:')
	dollar = int(dollar.replace(',', ''))
	products.append([name, dollar])
print(products)

for p in products:
	print(p[0], 'is', p[1], 'dollars')

with open ('products.csv', 'w') as f:
	f.write('Products, Price' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')