# http://usaco.org/index.php?page=viewproblem2&cpid=1036
from math import fabs


def rem(list, phrase):
    for g in range(len(list)):
        list[g] = list[g].strip(phrase)
    return list


def rev(tri):
    for g in range(len(tri)):
        tri[g].reverse()
    return(tri)


def rnum(oind, cow_max, full_data):
    r_pos = []
    for g in oind:
        i = full_data.index([g, 0])
        if i == cow_max-1:
            if full_data[i-1][1] == 1:
                r_pos.append(fabs(full_data[i][0] - full_data[i-1][0]))
        elif i == 0:
            if full_data[i+1][1] == 1:
                r_pos.append(fabs(full_data[i+1][0] - full_data[i][0]))
        else:
            if full_data[i+1][1] == 1:
                r_pos.append(fabs(full_data[i+1][0] - full_data[i][0]))
            if full_data[i-1][1] == 1:
                r_pos.append(fabs(full_data[i][0] - full_data[i-1][0]))
    r_pos.sort()
    print(r_pos)
    return(r_pos[0])


ind = []
oind = []
with open('socdist2.in', 'r') as w:
    t = w.readlines()
    t = rem(t, '\n')
    cow_num = int(t[0])
    t.pop(0)
    f = []
    for g in t:
        cl = []
        cl.append(int(g.partition(' ')[0]))
        ind.append(int(g.partition(' ')[0]))
        cl.append(int(g.partition(' ')[2]))
        f.append(cl)
    ind.sort()
    f.sort(reverse=True)
    max_position = f[0][0]
    f.sort()
    f = rev(f)
    for g in f:
        if g[0] == 0:
            oind.append(g[1])
    f = rev(f)
    l = []
    r = int(rnum(oind, cow_num, f) - 1)
    for g in range(len(f)):
        if g == cow_num-1:
            pass
        else:
            l.append([f[g][0], f[g+1][0] - f[g][0]])
c = 0
e = 0
for g in l:
    if g[1] > r:
        c += 1
for g in range(len(oind)):
    if g == len(oind) - 1:
        pass
    elif oind[g+1] - oind[g] > r:
        e += 1
with open('socdist2.out', 'w') as s:
    s.write(str(c-e))
