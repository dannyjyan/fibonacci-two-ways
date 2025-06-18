def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for n in test_values:
        result = fibonacci(n)
        print(f"Fibonacci({n}) = {result}")

