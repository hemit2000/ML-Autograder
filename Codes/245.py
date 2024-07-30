A = (1,2) 
B = (5,6)

def short_path(p1, p2):
    x_dist = abs(p2[0] - p1[0])
    y_dist = abs(p2[1] - p1[1])
    manh_dist = x_dist + y_dist
    return manh_dist

print(short_path(A, B))
