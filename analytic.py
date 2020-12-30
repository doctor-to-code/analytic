data = []
with open('reviews.txt', 'r') as f:
	data = [line for line in f ]

print(len(data))
good = [g for g in data if 'good' in g]
print(len(good))

fuck = [d for d in data if 'fuck' in d]
print(len(fuck))

love = [l for l in data if 'love' in l]
print(len(love))

fast = [l for l in data if 'fast' in l]
print(len(fast))
