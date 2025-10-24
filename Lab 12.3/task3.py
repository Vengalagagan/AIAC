def solve_linear_programming():
    """
    Solve the linear programming problem:
    Maximize: 3x + 5y
    Subject to: 2x + 3y <= 12, x + y <= 5, x >= 0, y >= 0
    """
    print("Linear Programming Problem:")
    print("Maximize: 3x + 5y")
    print("Subject to:")
    print("  2x + 3y <= 12")
    print("  x + y <= 5")
    print("  x >= 0, y >= 0")
    print("=" * 40)
    
    # Find feasible region by checking constraint intersections
    # Constraint 1: 2x + 3y = 12
    # Constraint 2: x + y = 5
    
    # Find intersection point
    # From constraint 2: y = 5 - x
    # Substituting into constraint 1: 2x + 3(5-x) = 12
    # 2x + 15 - 3x = 12
    # -x = -3
    # x = 3, y = 2
    
    intersection_x = 3
    intersection_y = 2
    
    # Check if intersection point is feasible
    if (2 * intersection_x + 3 * intersection_y <= 12 and 
        intersection_x + intersection_y <= 5 and 
        intersection_x >= 0 and intersection_y >= 0):
        
        intersection_feasible = True
        intersection_value = 3 * intersection_x + 5 * intersection_y
    else:
        intersection_feasible = False
        intersection_value = 0
    
    # Check corner points of feasible region
    corner_points = []
    
    # Point 1: (0, 0)
    if 2*0 + 3*0 <= 12 and 0 + 0 <= 5:
        corner_points.append((0, 0, 3*0 + 5*0))
    
    # Point 2: (0, 4) - from constraint 1: 2*0 + 3*y = 12, y = 4
    if 2*0 + 3*4 <= 12 and 0 + 4 <= 5:
        corner_points.append((0, 4, 3*0 + 5*4))
    
    # Point 3: (5, 0) - from constraint 2: x + 0 = 5, x = 5
    if 2*5 + 3*0 <= 12 and 5 + 0 <= 5:
        corner_points.append((5, 0, 3*5 + 5*0))
    
    # Point 4: (6, 0) - from constraint 1: 2*x + 3*0 = 12, x = 6
    if 2*6 + 3*0 <= 12 and 6 + 0 <= 5:
        corner_points.append((6, 0, 3*6 + 5*0))
    
    # Add intersection point if feasible
    if intersection_feasible:
        corner_points.append((intersection_x, intersection_y, intersection_value))
    
    # Find the point with maximum objective value
    if corner_points:
        optimal_point = max(corner_points, key=lambda point: point[2])
        optimal_x, optimal_y, optimal_value = optimal_point
        
        print(f"Corner points evaluated:")
        for x, y, value in corner_points:
            print(f"  ({x}, {y}) -> objective value: {value}")
        
        print(f"\nOptimal solution:")
        print(f"x = {optimal_x}")
        print(f"y = {optimal_y}")
        print(f"Maximum profit = {optimal_value}")
        
        return optimal_x, optimal_y, optimal_value
    else:
        print("No feasible solution found!")
        return None, None, None

if __name__ == "__main__":
    solve_linear_programming()
