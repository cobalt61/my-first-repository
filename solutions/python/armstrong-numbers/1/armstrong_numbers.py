"""Determine whether a number is an armstrong number or not."""
def get_digits_in_number(number):
    """Return the amount of digits in a number."""
    digits = 0
    while number > 0:
        number = number // 10
        digits += 1
    return digits
        

def is_armstrong_number(number):
    """Return true or false depending on whether the number is an armstrong number or not."""
    sum_of_numbers = 0
    number_mod = 0
    original_number = number
    digits_in_number = get_digits_in_number(original_number)
    for digit in range(digits_in_number):
        number_mod = number % 10
        sum_of_numbers += number_mod ** digits_in_number
        number = number // 10
    return sum_of_numbers == original_number
