def create_add_function():
    return lambda a, b: a + b

add_function = create_add_function()

result = add_function(5, 7)
print(result)  # 出力: 12

