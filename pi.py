import math

def get_nth_digit_of_pi(n):
    """
    This function returns the nth digit of Pi.
    
    Parameters:
    n (int): The position of the digit to retrieve
    
    Returns:
    int: The nth digit of Pi
    """
    try:
        # Check if the argument is a positive integer
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer")
        
        # Calculate Pi to the desired precision
        pi = str(math.pi)
        
        # Check if the requested digit is within the range of Pi
        if n > len(pi):
            raise ValueError("n exceeds the number of digits in Pi")
        
        # Retrieve and return the nth digit of Pi
        digit = int(pi[n-1])
        return digit
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return None
