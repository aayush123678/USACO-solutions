# http://usaco.org/index.php?page=viewproblem2&cpid=1011

from math import fabs


def rem(list, phrase):
    for g in range(len(list)):
        list[g] = list[g].strip(phrase)
    return list


def allsame_x(points, given_x):
    listofsame = []
    for g in range(len(points)):
        if points[g][0] == given_x:
            listofsame.append(g)
    return listofsame


def allsame_y(points, given_y):
    listofsame = []
    for g in range(len(points)):
        if points[g][1] == given_y:
            listofsame.append(g)
    return listofsame

# Finds the largest line given a grid and point
def largest_distance(points, index_decider, point_num_x, point_num_y):
    distance = -5
    if index_decider == 0:
        listofsame = allsame_y(points, point_num_y)
        for ind in listofsame:
            if fabs(point_num_x - points[ind][index_decider]) > distance:
                distance = fabs(point_num_x - points[ind][index_decider])
        return distance
    else:
        listofsame = allsame_x(points, point_num_x)
        for ind in listofsame:
            if fabs(point_num_y - points[ind][index_decider]) > distance:
                distance = fabs(point_num_y - points[ind][index_decider])
        return distance


def Rev_sort(points, index, rever):
    points.sort(key=lambda x: x[index], reverse=rever)


def tri_maker(points, pointx, pointy):
    dis_x = largest_distance(points, 0, pointx, pointy)
    dis_y = largest_distance(points, 1, pointx, pointy)
    return dis_x * dis_y


# gets the values from the file
with open("triangles.in", "r") as points:
    points = points.readlines()
    rem(points, '\n')
# converts values into useable ones (basically listed integers in a list)
num_points = int(points[0])
points.pop(0)
points = [points[g].split() for g in range(num_points)]
for g in range(num_points):
    points[g][0] = int(points[g][0])
    points[g][1] = int(points[g][1])
# takes each point and finds the area of the largets triangle, if an area is larger then the current largest one then it updates the area to that. 
triangle_area = -2
for point in points:
    a = tri_maker(points, point[0], point[1])
    if a > triangle_area:
        triangle_area = a

with open('triangles.out', 'w') as s:
    s.write(str(int(triangle_area)))
