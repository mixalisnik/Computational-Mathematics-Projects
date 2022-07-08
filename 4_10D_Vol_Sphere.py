import numpy as np



count = 0 # Count how many points are in sphere of dim with radius 1
grid_points=100000
dim=10
for point in range(grid_points):
    point1 = np.random.uniform(-1.0, 1.0, dim)
    distance = np.linalg.norm(point1)
    if distance < 1:
        count += 1

vol=np.power(2, dim) * (count / grid_points)
print("Volume of a ",dim,"-D sphere is : ", vol)