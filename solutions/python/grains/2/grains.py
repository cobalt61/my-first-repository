"""
Figure out how many grains are on squares, either in total or one at a time.
"""
def square(number):
    """Return the number of grains on one specific square."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """Return the total number of grains in all 64 squares."""
    total_grains = 0
    for square_number in range(64):
        total_grains = total_grains + 2 ** square_number
    return total_grains