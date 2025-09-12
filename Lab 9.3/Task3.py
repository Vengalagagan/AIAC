def calculator():
    """Simple calculator with menu selection."""
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    """
    This is a basic calculator program.

    It shows a menu with 4 options:
    1. Add two numbers
    2. Subtract two numbers
    3. Multiply two numbers
    4. Divide two numbers

    The user picks one option by typing a number (1 to 4).
    Then the user enters two numbers.
    The program does the calculation and shows the result.

    If the user picks division and the second number is 0,
    it shows an error message (because we can't divide by zero).
    If the user picks a wrong option, it shows "Invalid choice".
    """
    choice = input("Select operation (1-4): ")
    
 
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
   
    if choice == '1':
        """
    Add two numbers.Parameters
    ----------
    a, b : int or float
        Numbers to add.
    Returns
    -------
    int or float
        Sum of a and b.
    """
        result = x + y
        print(f"{x} + {y} = {result}")
    elif choice == '2':
        """
        Subtract b from a.Parameters
    ----------
    a, b : int or float
        Numbers to subtract.
    Returns
    -------
    int or float
        a minus b.
    """
        result = x - y
        print(f"{x} - {y} = {result}")
    elif choice == '3':
        """
        Multiply two numbers.
        Parameters
        ----------
        a, b : int or float
        Numbers to multiply.
        Returns
        -------
        int or float
        a times b.
        """
        result = x * y
        print(f"{x} × {y} = {result}")
    elif choice == '4':
        """
        Divide a by b.
        Parameters
        ----------
        a, b : int or float
        Numbers to divide.
        Returns
        -------
        int or float
        a divided by b.
        """
        if y == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = x / y
            print(f"{x} ÷ {y} = {result}")
    else:
        print("Invalid choice!")

calculator()
