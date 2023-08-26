numbers = list(range(1, 11))

for func in [sum, min, max]:
    print(f"{func.__name__}: {func(numbers)}")

