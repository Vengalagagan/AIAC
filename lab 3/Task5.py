def temperature_conversion(temp, from_scale, to_scale):
    """
    Convert temperature between different scales (Celsius, Fahrenheit, Kelvin)
    
    Args:
        temp (float): Temperature value to convert
        from_scale (str): Original temperature scale ('C', 'F', or 'K')
        to_scale (str): Target temperature scale ('C', 'F', or 'K')
    
    Returns:
        float: Converted temperature value
    """
    # Convert to Celsius first (as intermediate step)
    if from_scale.upper() == 'C':
        celsius = temp
    elif from_scale.upper() == 'F':
        celsius = (temp - 32) * 5/9
    elif from_scale.upper() == 'K':
        celsius = temp - 273.15
    else:
        raise ValueError("Invalid 'from_scale'. Use 'C', 'F', or 'K'")
    
    # Convert from Celsius to target scale
    if to_scale.upper() == 'C':
        return celsius
    elif to_scale.upper() == 'F':
        return celsius * 9/5 + 32
    elif to_scale.upper() == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid 'to_scale'. Use 'C', 'F', or 'K'")

# Example usage and printing
if __name__ == "__main__":
    print("Temperature Conversion Examples:")
    print("=" * 40)
    
    # Test cases
    test_temps = [
        (25, 'C', 'F'),    # 25°C to Fahrenheit
        (98.6, 'F', 'C'),  # 98.6°F to Celsius
        (300, 'K', 'C'),   # 300K to Celsius
        (0, 'C', 'K'),     # 0°C to Kelvin
        (212, 'F', 'K'),   # 212°F to Kelvin
        (37, 'C', 'F')     # 37°C to Fahrenheit
    ]
    
    for temp, from_scale, to_scale in test_temps:
        try:
            converted_temp = temperature_conversion(temp, from_scale, to_scale)
            print(f"{temp}°{from_scale} = {converted_temp:.2f}°{to_scale}")
        except ValueError as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 40)
    
    # Interactive example
    print("\nInteractive Temperature Conversion:")
    try:
        user_temp = float(input("Enter temperature value: "))
        user_from = input("Enter source scale (C/F/K): ").upper()
        user_to = input("Enter target scale (C/F/K): ").upper()
        
        result = temperature_conversion(user_temp, user_from, user_to)
        print(f"\n{user_temp}°{user_from} = {result:.2f}°{user_to}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
