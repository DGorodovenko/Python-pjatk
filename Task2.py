shapes = []

while True:
    input_str = input("Enter one, two or three numbers (or 'q' to quit): ")

    if input_str == ' ':
        break

    numbers = input_str.split()

    # Create a tuple with three elements
    if len(numbers) == 1:
        shape = 'S'
        dimensions = (float(numbers[0]),)
        area = float(numbers[0]) ** 2
    elif len(numbers) == 2:
        shape = 'R'
        dimensions = (float(numbers[0]), float(numbers[1]))
        area = float(numbers[0]) * float(numbers[1])
    elif len(numbers) == 3:
        shape = 'C'
        dimensions = (float(numbers[0]), float(numbers[1]), float(numbers[2]))
        area = float(numbers[0]) * float(numbers[1]) * float(numbers[2])
    else:
        print("Invalid input: please enter one, two, or three numbers.")
        continue

    tuple_ = (shape, dimensions, area)

    # Add the tuple to the list of shapes
    shapes.append(tuple_)

    # Print the tuple
    print(shapes)


