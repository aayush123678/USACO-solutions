# http://usaco.org/index.php?page=viewproblem2&cpid=808

def rem(list, phrase):
    for g in range(len(list)):
        list[g] = list[g].strip(phrase)
    return list


def lcompare(w, g, max):
    if g == 0:
        return False
    elif g == max-1:
        return True
    elif w[g] - w[g-1] < w[g+1] - w[g]:
        return True
    elif w[g] - w[g-1] == w[g+1] - w[g]:
        return True
    else:
        return False


pass_back = []
pass_forward = []
t = []
b = 0
last_ind = 0
with open('hoofball.in', 'r') as w:
    w = w.readlines()
    w = rem(w, '\n')
    cows = int(w[0])
    w.pop(0)
    w = w[0].split(' ')
    for g in range(cows):
        w[g] = int(w[g])
    w.sort()
    for g in range(cows):
        if g == cows-1:
            if w[g-1] in pass_back:
                t.append(w[last_ind:g+1])
        elif lcompare(w, g, cows):
            pass_back.append(w[g])
        elif not lcompare(w, g, cows):
            pass_forward.append(w[g])
            if g+1 == cows-1:
                t.append([w[g], w[g+1]])
            if w[g-1] in pass_back:
                t.append(w[last_ind:g])
                last_ind = g
for i in t:
    a = len(i)
    if a == 2:
        b += 1
    elif lcompare(i, 1, a) or not lcompare(i, -2, a):
        b += 1
    else:
        b += 2

with open('hoofball.out', 'w') as e:
    e.write(str(b))
