def tableau_creator() -> str:
    """Takes user input on number of variables, 
    number of constraints, and variables letters in the form of (xyz)
    to return the final tableau with the cost in the corner.

    Returns:
        str: Tableaus of the maximization problem
        using the simplex method.
    """
    num_variables = int(input("Enter the number of variables: "))
    variables = str(input("Enter the variables: "))
    constraints = int(input("Enter the number of constraints: "))
    
    tableau_header = ["   ", "|   "]
    for char in variables:
        tableau_header.insert(-1, "| " + char + " ")
    for i in range(constraints):
        tableau_header.insert(-1, "| " + "x_" + str(i))
    
    return tableau_header

if __name__ == "__main__":
    print(tableau_creator())