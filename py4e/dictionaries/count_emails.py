name = input("Enter file:\n")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emails = {}

for line in handle:
    if line.startswith('From '):
        emailAddress = line.split(' ')[1]
        emails[emailAddress] = emails.get(emailAddress, 0) + 1

maximum = None
for email, count in emails.items():
    if maximum is None:
        maximum = (email, count)
    elif count > maximum[1]:
        maximum = (email, count)
print(maximum[0], maximum[1])