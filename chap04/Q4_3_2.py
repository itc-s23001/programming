def square_numbers(numbers):
    return [num ** 2 for num in numbers]

large_numbers = list(range(1, 101))
large_squared_result = square_numbers(large_numbers)
print(large_squared_result)

