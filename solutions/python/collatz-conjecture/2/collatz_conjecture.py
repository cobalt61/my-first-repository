def steps(number):
    """
    Description: 
    This function returns the amount of steps to solve the collatz conjecture for a specific number.
    If that number is zero or below, a ValueError is raised.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_taken = 0
    while number > 1:
        is_even = number % 2 == 0
        if is_even:
            number /= 2
        else:
            number *= 3
            number += 1
        steps_taken += 1
    return steps_taken
