data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data. append(line)
		count += 1
		if count % 10000 == 0: #count/1000餘數是0的意思:每一千筆記錄一次意思
			print(len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '留言長度小於100')
print(new[10])