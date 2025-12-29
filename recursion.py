#factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

#sum using recusrsion 
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print("Sum:", sum_numbers(5))
