def factorial(n):
    if n < 0:
        return ("[-] Factorial of negative numbers is not defined")
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(0))
    print(factorial(-2))