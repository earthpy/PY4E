fh = open('romeo.txt')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wds = dict()
lst = list()
found = None
for line in fh:
    line = line.lower()
    line = line.rstrip()
    temp = list(line)
    for w in temp:

        for i in letters:
            if w == i:
                found = False
                break
            else:
                found = True
                continue

        if found == True:
            continue
        else:
            lst.append(w)
            wds[w] = wds.get(w, 0) + 1

tmp = list()
counter = 0
for word,count in wds.items():
    counter += count
    tmp.append((count,word))

tmp = sorted(tmp, reverse=True)
for count,word in tmp:
    print('Letter:', word, '| Count:', count, '| Freq.(%):', (count/counter)*100)
