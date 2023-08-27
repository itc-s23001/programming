def show_begin_end(func):
    def wrapper(*args, **kwargs):
        print("==begin")
        result = func(*args, **kwargs)
        print("==end")
        return result
    return wrapper

@show_begin_end
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)  

