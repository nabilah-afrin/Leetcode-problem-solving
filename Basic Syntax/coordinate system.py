def create_coordinate_system(width, height):
    # Initialize a 2D list to represent the coordinate system
    coordinate_system = [[' ' for _ in range(width)] for _ in range(height)]

    # Draw the axes
    for i in range(width):
        coordinate_system[height // 2][i] = '-'
    for i in range(height):
        coordinate_system[i][width // 2] = '|'

    # Set the origin
    coordinate_system[height // 2][width // 2] = 'O'

    return coordinate_system

# Example: Create a 10x10 coordinate system
width, height = 10, 10
coordinate_system = create_coordinate_system(width, height)

# Print the coordinate system
for row in coordinate_system:
    print(' '.join(row))
