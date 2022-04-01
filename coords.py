BRICK_COORDS = []
for y in range(-50, 250, 20):
    # brick.goto(-425, y / 2.4)
    for x in range(-425, 450, 40):
        brick_coord = (x, y)
        BRICK_COORDS.append(brick_coord)
print(len(BRICK_COORDS))