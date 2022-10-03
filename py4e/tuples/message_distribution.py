name = input("Enter file:\n")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}

for line in handle:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1
for k, v in sorted(counts.items()):
    print(k, v)