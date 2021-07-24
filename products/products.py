import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'Products, Price' in line:
				continue #繼續 ＃跳過這一回
			name, dollar = line.strip().split(',')
			products.append([name, dollar])
	return products
		
#讓使用者輸入
def user_input(products):
	while True:
		name = input('What did you buy:')
		if name == 'q':
			break
		dollar = input('How much was it:')
		dollar = int(dollar.replace(',', ''))
		products.append([name, dollar])
	print(products)
	return products

#印出所有購買紀錄
def prints_products(products):
	for p in products:
		print(p[0], 'is', p[1], 'dollars')

#寫入檔案
def write_file(filename, products):
	with open (filename, 'w') as f:
		f.write('Products, Price' + '\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('yap, file found!')
		products = read_file(filename)
	else:
		print('file not found...')
		
	products = user_input(products)
	prints_products(products)
	write_file('products.csv', products)


main()