import re
fh = open('data.txt', 'r')

sum = 0

for line in fh:
    for match in re.findall('[0-9]+', line):
        sum = sum + int(match)
print(sum)