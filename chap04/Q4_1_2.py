def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while (next_fib := fib_sequence[-1] + fib_sequence[-2]) <= n:
        fib_sequence.append(next_fib)
    return fib_sequence

# 例として引数として10を渡す場合
result = fibonacci_sequence(10)
print(result)

