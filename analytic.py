data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data. append(line)
		count += 1
		if count % 10000 == 0: #count/1000餘數是0的意思:每一千筆記錄一次意思
			print(len(data))
print(len(data))
print(data[5])
print('----------------------------------')
print(data[15])
print('----------------------------------')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(sum_len)
k = sum_len/len(data)
print(k)