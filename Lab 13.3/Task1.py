

#improve the above python code readability, efficiency, and error handling with refactoring it with dictionary-based dispatch or separate functions
_AREA_DISPATCH = {
    "rectangle": area_rectangle,
    "square": area_square,
    "circle": area_circle,
}

def area_rectangle(width, height):
    _validate_positive_number(width, "width")
    _validate_positive_number(height, "height")
    return width * height
def area_square(side):
    _validate_positive_number(side, "side")
    return side * side
def area_circle(radius):
    _validate_positive_number(radius, "radius")
    return 3.14 * radius * radius   
def _validate_positive_number(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{name} must be > 0, got {value}")
def calculate_area(shape, x, y=0):
    return _AREA_DISPATCH[shape](x, y)

    print(calculate_area("rectangle", 10, 20))
    print(calculate_area("square", 10))
    print(calculate_area("circle", 10))












