def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

number = int(input("上限の数を入力してください: "))
result = fibonacci_sequence(number)
print(result)

