""" fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        count += 1
        ln = line.split(' ') 
        print(ln[1])
print("There were", count, "lines in the file with From as the first word") """

fname = input("Enter file name: ")
fh = open(fname)
lst= []
counts = dict()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    if len(wds) <3 or wds[0] != 'From':
        continue
    ts = wds[1]
    lst.append(ts)
for word in lst:
    counts[word] = counts.get(word,0) + 1
#print('Counts', counts)
#print(lst)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)