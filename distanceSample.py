coordinates = [(1,1), (2,2), (3,3), (4,4), (5,5)]

x = 1.8
y = -2.5

distances = []

# compute squared distances 
for cx, cy in coordinates:
    d = (x - cx)**2 + (y - cy)**2
    distances.append(d)

# find smallest distance
nearest_index = 0
for i in range(1, len(distances)):
    if distances[i] < distances[nearest_index]:
        nearest_index = i

print("Distances:", distances)
print("Nearest index:", nearest_index)
print("Nearest coordinate:", coordinates[nearest_index])