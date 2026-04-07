# Function to check if a number is even
def is_even(num):
    """
    Check if a number is even.
    
    Args:
        num: An integer to check
    
    Returns:
        True if the number is even, False otherwise
    """
    if num % 2 == 0:
        return True
    else:
        return False


# Alternative concise version
def is_even_short(num):
    return num % 2 == 0


# Test cases
if __name__ == "__main__":
    # Test with different numbers
    numbers = [4, 7, 10, 15, 20, 23, 0, -4, -7]
    
    for num in numbers:
        if is_even(num):
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")
