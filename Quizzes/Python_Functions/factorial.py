def factorial(num):
    """The factorial of a number is the product of all the integers from 1 to that number"""
    if num < 0:
        print(f'No factorial for {num} and other negative numbers.')
    else:
        num += 1
        fact = 1
        for i in range(1, num):
            fact = fact * i

        print(f'The factorial of {num-1} is ({fact})')

factorial(5)