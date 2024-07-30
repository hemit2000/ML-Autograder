def cube_info(edge_length):
    area = 6 * edge_length**2
    volume = edge_length**3
    return area,volume

edge_length = 3
area, volume = cube_info(edge_length)
print("Area of the Cube:", area)
print("Volume of the Cube:", volume)
