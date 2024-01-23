num_points = int(input())

count = 0

xc = []
yc = []

points = {}

for i in range(num_points):
    coords = input().split()
    coords[0] = int(coords[0])
    coords[1] = int(coords[1])
    point = (coords[0], coords[1])
    xc.append(coords[0])
    yc.append(coords[1])
    points[point] = 0
        
for i in range(num_points):
    
    point = (xc[i], yc[i])
    # del points(point)
    
    p1 = (xc[i], yc[i] + 2018)
    p2 = (xc[i] + 2018, yc[i])
    p3 = (xc[i], yc[i] - 2018)
    p4 = (xc[i] - 2018, yc[i])
    p5 = (xc[i] + 1118, yc[i] + 1680)
    p6 = (xc[i] - 1118, yc[i] - 1680)
    p7 = (xc[i] - 1118, yc[i] + 1680)
    p8 = (xc[i] + 1118, yc[i] - 1680)
    
    p9 = (xc[i] + 1680, yc[i] - 1118)
    p10 = (xc[i] - 1680, yc[i] - 1118)
    p11 = (xc[i] - 1680, yc[i] + 1118)
    p12 = (xc[i] + 1680, yc[i] + 1118)
    
    c = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    # if i == 3: 
    #     print(c)
    #     print(points)
    for p in c:
        if points.get(p) is not None:
            # print(p, points, c)
            count += 1
    
# print(count / 2)
count = int(count / 2)
print(count)
        
    