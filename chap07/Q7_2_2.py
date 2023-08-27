def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("引数は整数または小数である必要があります。")
    return x ** 2

try:
    result = square(5)
    print(result) 

    result = square(2.5)
    print(result)  

    result = square("abc")  
    print(result)
except TypeError as e:
    print("エラー:", e)

