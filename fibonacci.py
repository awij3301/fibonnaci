"""
Fibonacci Sequence Implementation in Python

This module contains multiple implementations of the Fibonacci sequence:
1. Recursive approach
2. Iterative approach
3. Generator approach
4. Memoized recursive approach
"""

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Note: This approach has exponential time complexity O(2^n)
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_generator(count):
    """
    Generate Fibonacci numbers using a generator.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
    
    Yields:
        int: Next Fibonacci number in the sequence
    """
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def fibonacci_memoized(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
        memo (dict): Cache for previously calculated values
    
    Returns:
        int: The nth Fibonacci number
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_sequence(count):
    """
    Generate a list of the first 'count' Fibonacci numbers.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: List of Fibonacci numbers
    """
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def is_fibonacci(num):
    """
    Check if a number is a Fibonacci number.
    
    A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
    """
    import math
    
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


def main():
    """
    Demonstrate different Fibonacci implementations.
    """
    print("Fibonacci Sequence Implementations\n")
    
    n = 10
    print(f"First {n} Fibonacci numbers:")
    
    # Using generator
    print("Using generator:")
    fib_gen = fibonacci_generator(n)
    print([next(fib_gen) for _ in range(n)])
    
    # Using sequence function
    print("\nUsing sequence function:")
    print(fibonacci_sequence(n))
    
    # Individual calculations
    print(f"\nFibonacci number at position {n-1}:")
    print(f"Recursive: {fibonacci_recursive(n-1)}")
    print(f"Iterative: {fibonacci_iterative(n-1)}")
    print(f"Memoized: {fibonacci_memoized(n-1)}")
    
    # Check if numbers are Fibonacci
    print(f"\nChecking if numbers are Fibonacci:")
    test_numbers = [0, 1, 2, 3, 4, 5, 8, 13, 21, 34, 35]
    for num in test_numbers:
        print(f"{num}: {is_fibonacci(num)}")


if __name__ == "__main__":
    main()
