import sympy as sp
# Define the symbol
x = sp.symbols('x')
# Define the function
f = 2 * x**3 + 4 * x + 5

# Find the derivative
f_prime = sp.diff(f, x)

# Solve f'(x) = 0 for critical points
critical_points = sp.solve(f_prime, x)

# Filter out complex solutions and keep only real ones
real_critical_points = []
for point in critical_points:
    if point.is_real:
        real_critical_points.append(point)

# For a cubic function, check each real critical point to see which gives a minimum
min_x = None
min_value = None

if real_critical_points:
    for point in real_critical_points:
        # Second derivative test
        f_double_prime = sp.diff(f_prime, x)
        second_derivative = f_double_prime.subs(x, point)
        if second_derivative > 0:
            value = f.subs(x, point)
            min_x = point
            min_value = value
            break  # In real cubic, at most one minimum
else:
    # If no real critical points, the function has no local minima
    # For a cubic function f(x) = 2x^3 + 4x + 5, since f'(x) = 6x^2 + 4 > 0 for all real x,
    # the function is strictly increasing and has no local minima
    print("The function f(x) = 2x^3 + 4x + 5 has no local minima.")
    print("The derivative f'(x) = 6x^2 + 4 is always positive for real x.")
    print("The function is strictly increasing and approaches -infinity as x approaches -infinity.")
    min_x = "No local minimum exists"
    min_value = "Function approaches -infinity as x approaches -infinity"

print("The value of x at which f(x) = 2x^3 + 4x + 5 is minimum is:", min_x)
