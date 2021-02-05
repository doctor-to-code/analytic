import time

start_time =  time.time()

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count+=1
		if count % 1000 == 0:
			print(len(data))
print('總共有', len(data), '筆資料')

print(data[1])

wc = {} #word count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增一個字進字典
			             #
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Peter'])

while True:
	word = input('請問你想查什麼字')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過次數為:', wc[word])
	else:
		print('沒有出現過這個字')

print('感謝使用，再見囉')