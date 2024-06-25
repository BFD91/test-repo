def calculate_fibonacci():
    fib_list = [0, 1]  # Initialize with the first two Fibonacci numbers
    while len(fib_list) < 10:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# Example usage:
fibonacci_numbers = calculate_fibonacci()
print(fibonacci_numbers)
