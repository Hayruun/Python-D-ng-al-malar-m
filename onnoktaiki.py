fname = input("Enter file name: ")
fh = open(fname)
lst= list()
counts = dict()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) <3 or wds[0] != 'From':
        continue
    ts = wds[5]
    ts = ts[:2]
    lst.append(ts)
for word in lst:
    counts[word] = counts.get(word,0) + 1
for key,value in sorted(counts.items()):
    print(key, value)


