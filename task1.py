def caching_fibonacci():
    """
    Factory function that returns a memoized Fibonacci function.
    The returned function computes Fibonacci numbers efficiently by caching
    previously computed values, thus avoiding redundant recursive calculations.
    Returns:
        function: A fibonacci(n) function that computes the nth Fibonacci number
                 with memoization. The function accepts a non-negative integer n
                 and returns the nth Fibonacci number where:
                 - fibonacci(0) = 0
                 - fibonacci(1) = 1
                 - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1
    """

    #initialize the cache to store previously computed Fibonacci values
    cache = {}

    def fibonacci(n):
        
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        #if the Fibonacci value for n is already stored in the cache, return it
        if n in cache:
            return cache[n]
        
        #if the Fibonacci value for n is not in the cache, compute it recursively and store it in the cache
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        
        return result

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610