data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data. append(line)
		count += 1
		if count % 10000 == 0: #count/1000餘數是0的意思
			print(len(data))
print(len(data))
print(data[5])
print('----------------------------------')
print(data[15])
print('----------------------------------')
