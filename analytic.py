data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data. append(line)
print(len(data))
good = [g for g in data if 'good' in g]
print(len(good))

fuck = [d for d in data if 'fuck' in d]
print(len(fuck))

love = [l for l in data if 'love' in l]
print(len(love))