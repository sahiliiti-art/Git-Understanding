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


# Function to check if a number is prime
def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num: An integer to check
    
    Returns:
        True if the number is prime, False otherwise
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


# Function to check if a number is a palindrome
def is_palindrome(num):
    """
    Check if a number is a palindrome.
    
    Args:
        num: An integer to check
    
    Returns:
        True if the number reads the same forwards and backwards, False otherwise
    """
    if num < 0:
        return False
    string_num = str(num)
    return string_num == string_num[::-1]


# Test cases
if __name__ == "__main__":
    # Test with different numbers
    numbers = [4, 7, 10, 15, 20, 23, 0, -4, -7]
    
    print("Testing even numbers:")
    for num in numbers:
        if is_even(num):
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")
    
    print("\nTesting prime numbers:")
    for num in numbers:
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
    
    print("\nTesting palindrome numbers:")
    for num in numbers:
        if is_palindrome(num):
            print(f"{num} is a palindrome")
        else:
            print(f"{num} is not a palindrome")
