memo = {}

def fibonacci_recursive(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    memo[n] = result
    return result


def fibonacci_non_recursive(n):
    memo = {}
    for i in range(1, n+1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


print(fibonacci_recursive(5))
print(fibonacci_recursive(10))
print(fibonacci_recursive(50))

print(fibonacci_non_recursive(5))
print(fibonacci_non_recursive(10))
print(fibonacci_non_recursive(50))



