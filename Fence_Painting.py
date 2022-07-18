#http://www.usaco.org/index.php?page=viewproblem2&cpid=567
import os


def overlap(f, b):
    for e in range(2):
        f[e] = int(f[e])
    for e in range(2):
        b[e] = int(b[e])
    if max(f) < min(b) or max(b) < min(f):
        return False
    else:
        return True


with open("paint.in", "r") as f:
    with open("paint.out", "a") as g:
        fj = f.readlines(1)[0].split(" ")
        bj = f.readlines(0)[0].split(" ")
        fj[1] = fj[1].replace("\n", "")
        if overlap(fj, bj):
            l = fj + bj
            for i in range(len(l)):
                l[i] = int(l[i])
            g.write(str(max(l) - min(l)))
        else:
            for i in range(len(fj)):
                fj[i] = int(fj[i])
            for i in range(len(bj)):
                bj[i] = int(bj[i])
            g.write(str((max(fj) - min(fj)) + (max(bj) - min(bj))))
