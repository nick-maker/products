products = []

#讀取檔案
with open('products.csv', 'r') as f:
	for line in f:
		if 'Products, Price' in line:
			continue #繼續 ＃跳過這一回
		name, dollar = line.strip().split(',')
		products.append([name, dollar])
print(products)

#讓使用者輸入
while True:
	name = input('What did you buy:')
	if name == 'q':
		break
	dollar = input('How much was it:')
	dollar = int(dollar.replace(',', ''))
	products.append([name, dollar])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], 'is', p[1], 'dollars')

#寫入檔案
with open ('products.csv', 'w') as f:
	f.write('Products, Price' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')