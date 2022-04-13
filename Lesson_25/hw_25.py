def square(x):
    return x * x

  

def cube(x):
    return x * x * x


def my_map(function, list_of_numbers):
    result = []
    for number in list_of_numbers:
        result.append(function(number))
    return result


list_of_squares = my_map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list_of_squares)

list_of_cubes = my_map(cube, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list_of_cubes)
