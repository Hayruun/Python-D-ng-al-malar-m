fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = fh.read()
    line = line.split()
line = list(set(line)) 
line.sort()
print(line)
