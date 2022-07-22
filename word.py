# http://www.usaco.org/index.php?page=viewproblem2&cpid=987
import copy


def rem(list, phrase):
    for g in range(len(list)):
        list[g] = list[g].strip(phrase)
    return list


procc = []
s = []
with open('word.in', 'r') as w:
    w = w.readlines()
    w = rem(w, '\n')
    w[0].split(' ')
    wordnum, lim, para = int(w[0].split()[0]), int(
        w[0].split()[1]), w[1].split()
lims = [len(para[word]) for word in range(wordnum)]
n = 0
e = []
for a in range(wordnum):
    if a == wordnum - 1:
        if n+lims[a] <= lim:
            e.append(para[a])
            procc.append(e)
        else:
            procc.append(e)
            procc.append([para[a]])
    elif n+lims[a] <= lim:
        e.append(para[a])
        n += lims[a]
    else:
        n = 0
        procc.append(copy.deepcopy(e))
        e.clear()
        e.append(para[a])
        n = len(para[a])
with open('word.out', 'w') as w:
    for g in procc:
        for i in range(len(g)):
            if i == len(g)-1:
                w.write(g[i] + '\n')
                print(g[i])
            else:
                w.write(g[i]+' ')
                print(g[i], end=' ')
