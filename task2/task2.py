import math
import sys


def read_circle_data(filename):
    with open(filename, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius


def read_dots_data(filename):
    dots = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            dots.append((x, y))
    return dots


def check_dot_position(center, radius, dot):
    center_x, center_y = center
    dot_x, dot_y = dot
    distance_squared = (dot_x - center_x) ** 2 + (dot_y - center_y) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    elif distance_squared == radius_squared:
        return 0  # Точка лежит на окружности
    else:
        return 2  # Точка снаружи окружности


def main(circle_data, dots_data):
    center_x, center_y, radius = read_circle_data(circle_data)
    dots = read_dots_data(dots_data)

    results = []
    for dot in dots:
        result = check_dot_position((center_x, center_y), radius, dot)
        results.append(result)

    for res in results:
        print(res)


if __name__ == "__main__":
    circle_file = sys.argv[1]
    dots_file = sys.argv[2]

    main(circle_file, dots_file)

