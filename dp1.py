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


def fibonacci_loop(n):
    memo = {}
    for i in range(1, n+1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


# print(fibonacci_recursive(5))
# print(fibonacci_recursive(10))
# print(fibonacci_recursive(50))
#
# print(fibonacci_loop(5))
# print(fibonacci_loop(10))
# print(fibonacci_loop(50))


def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

memo = {}
def minimum_coins_recursive(m, coins) -> int:
    if m in memo:
        answer = memo[m]
    elif m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                continue
            answer = min_ignore_none(answer, minimum_coins_recursive(subproblem, coins) + 1)
    memo[m] = answer
    return answer


def minimum_coins_loop(m, coins) -> int:
    memo = {}
    memo[0] = 0
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return memo[m]


print(minimum_coins_recursive(13, [1, 4, 5]))
print(minimum_coins_recursive(150, [1, 4, 5]))

print(minimum_coins_loop(13, [1, 4, 5]))
print(minimum_coins_loop(150, [1, 4, 5]))


def how_many_ways_loop(m, coins) -> int:
    memo = {}
    memo[0] = 1
    for i in range(1, m + 1):
        memo[i] = 0
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = memo.get(i) + memo.get(subproblem)
    return memo[m]


print(how_many_ways_loop(13, [1, 4, 5]))
print(how_many_ways_loop(150, [1, 4, 5]))

memo = {}
def maze_recursive(n, m) -> int:
    if n > m:
        n, m = m, n
    if (n, m) not in memo:
        if n == 1:
            memo[n, m] = 1
        else:
            memo[n, m] = maze_recursive(n, m-1) + maze_recursive(n-1, m)
    return memo[n, m]


# print(maze_recursive(1, 1))
# print(maze_recursive(2, 2))
# print(maze_recursive(2, 3))
# print(maze_recursive(3, 2))
# print(maze_recursive(3, 3))

print(maze_recursive(106, 73))

def maze_loop(n, m) -> int:
    memo = {}
    # if n > m:
    #     n, m = m, n
    for i in range(1, n+1):
        memo[i, 1] = 1
    for j in range(1, m+1):
        memo[1, j] = 1
    for j in range(2, m+1):
        for i in range(2, n+1):
            memo[i, j] = memo[i-1, j] + memo[i, j-1]
    return memo[n, m]


print(maze_loop(1, 1))
print(maze_loop(2, 2))
print(maze_loop(2, 3))
print(maze_loop(3, 2))
print(maze_loop(3, 3))

print(maze_recursive(106, 73))