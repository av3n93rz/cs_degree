fname = input("Enter file name:\n")
try:
    fh = open(fname)
except:
    print("Error: file does not exists")
    quit()

count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    line = line.rstrip()
    value = value + float(line[line.find(' ') + 1:])
    
print("Average spam confidence:", value/count)